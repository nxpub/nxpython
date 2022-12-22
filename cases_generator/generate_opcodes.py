import os
import re
import sys
import argparse
import typing
import inspect

from cases_generator import parser
from cases_generator.generate_cases import Analyzer, Formatter
from cases_generator.generate_docs import fetch_docs


class PyFormatter(Formatter):

    def __init__(self, stream: typing.TextIO, indent: int) -> None:
        super().__init__(stream, indent)
        self._indent = indent
    
    def emit(self, arg: str, comment: bool = True) -> None:
        if arg:
            line = f'{self.prefix}{arg}\n'
            if comment:
                line = line[:self._indent] + '# ' + line[self._indent:]
            self.write_raw(line)
        else:
            self.write_raw('\n')

    def write_raw(self, s: str) -> None:
        # This tricky thing helps to fix a direct write_raw() call from Instruction.write_body
        if (prev_frame := inspect.stack()[1]).function == 'write_body':
            self.emit(s[-prev_frame.frame.f_locals['dedent']:].replace('\n', ''))
        else:
            super().write_raw(s)
            # TODO: Remove, was used for rt debugging
            self.stream.flush()


RE_OPCODE = re.compile(r'#define\s+(?P<name>[0-9A-Z_]+)\s+(?P<value>\d+)\n')


class DSLAnalyzer(Analyzer):

    def __init__(
        self, *,
        dsl_path: str,
        output_path: str,
        opcode_h_path: str,
        cpython_sha: str,
    ):
        super().__init__(filename=dsl_path, output_filename='')
        self.out = None
        self._cpython_sha = cpython_sha
        self._output_path = output_path
        self._docs = fetch_docs()
        # TODO: Use generate_opcode_h.py-like mechanism to generate from Lib/opcode.py
        with open(opcode_h_path) as opcode_h_file:
            self._opcodes = {
                name: value
                for name, value in RE_OPCODE.findall(opcode_h_file.read())
            }

    def _write_prologue(self, fp, thing):
        cls_title = ''.join(map(lambda p: p[0].title() + p[1:], filter(None, thing.name.lower().split('_'))))
        class_name = f'Op{cls_title}'
        fp.write(f'# Auto-generated via https://github.com/python/cpython/blob/{self._cpython_sha}/Python/bytecodes.c')
        fp.write('\n')
        fp.write(f'from .base import OpCode\n\n\n')
        fp.write(f'class {class_name}(OpCode):\n')
        fp.write(f'    """\n')
        if thing_doc := self._docs.get(thing.name):
            for line in thing_doc.splitlines():
                fp.write(f'    {line}\n')
            # TODO: Python version should be flexible in the url
            fp.write(f'\n    https://docs.python.org/3.12/library/dis.html#opcode-{thing.name}\n')
        else:
            fp.write(f'    TODO: Cannot find documentation via dis docs!\n')
        fp.write(f'    """\n')
        fp.write(f'    OPCODE_NAME = \'{thing.name}\'\n')
        fp.write(f'    OPCODE_VALUE = {self._opcodes[thing.name]}\n\n')
        fp.write(f'    def extract(self, stack) -> None:\n')
        fp.write(f'        raise NotImplementedError\n\n')
        # TODO: Avoid hasattr, do better
        if hasattr(thing, 'inputs'):
            args = ', '.join(['self'] + list(map(lambda effect: effect.name, thing.inputs)))
        else:
            args = 'self'
        fp.write(f'    def transform({args}) -> None:')

    @staticmethod
    def _write_epilogue(fp):
        fp.write(f'        raise NotImplementedError\n\n')
        fp.write(f'    def load(self, stack) -> None:\n')
        fp.write(f'        raise NotImplementedError\n')

    @staticmethod
    def _to_filename(opcode_name: str) -> str:
        return f'op_{opcode_name.lower()}.py'

    def _fix_instr(self, instr):
        # removes copied indents and line ends, TODO: do we need to fix tokens/positions?
        # TODO: Avoid magic const 12, it's pretty fragile if CPython folks will change the layout
        instr.block_text = list(map(lambda l: l[12:].replace('\n', ''), instr.block_text))
        return instr

    def _fix_super(self, super):
        return super

    def _fix_macro(self, macro):
        return macro

    def write_instructions(self) -> None:
        n_instrs = n_supers = n_macros = 0
        for thing in self.everything:
            if hasattr(thing, 'kind') and thing.kind == 'op':
                print('skipped', thing.name)
                continue
            with open(os.path.join(self._output_path, self._to_filename(thing.name)), 'w') as opcode_file:
                self._write_prologue(opcode_file, thing)
                self.out = PyFormatter(opcode_file, 8)
                match thing:
                    case parser.InstDef():
                        if thing.kind == "inst":
                            n_instrs += 1
                            self.write_instr(self._fix_instr(self.instrs[thing.name]))
                    case parser.Super():
                        n_supers += 1
                        self.write_super(self._fix_super(self.super_instrs[thing.name]))
                    case parser.Macro():
                        n_macros += 1
                        self.write_macro(self._fix_macro(self.macro_instrs[thing.name]))
                    case _:
                        typing.assert_never(thing)
                self._write_epilogue(opcode_file)
        print(
            f'Wrote {n_instrs} instructions, {n_supers} supers, '
            f'and {n_macros} macros to {self.output_filename}',
            file=sys.stderr,
        )


def _make_parser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        description='Generate the code for the interpreter switch.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    arg_parser.add_argument(
        '-i', '--input', type=str, help='Instruction definitions',
    )
    arg_parser.add_argument(
        '-o', '--output', type=str, help='Generated code',
    )
    arg_parser.add_argument(
        '--opcodes', type=str, help='Path to generated opcode.h',
    )
    arg_parser.add_argument(
        '--commit', type=str, help='CPython commit sha', default='main',
    )
    return arg_parser


def main():
    args = _make_parser().parse_args()
    analyzer = DSLAnalyzer(
        dsl_path=args.input, output_path=args.output, opcode_h_path=args.opcodes, cpython_sha=args.commit,
    )
    analyzer.parse()
    analyzer.analyze()
    if analyzer.errors:
        sys.exit(f'Found {analyzer.errors} errors')
    analyzer.write_instructions()


if __name__ == '__main__':
    main()
