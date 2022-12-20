# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpExtendedArg(BaseOpCode):
    """
    Prefixes any opcode which has an argument too big to fit into the default one
    byte. ext holds an additional byte which act as higher bits in the argument.
    For each opcode, at most three prefixal EXTENDED_ARG are allowed, forming
    an argument from two-byte to four-byte.

    https://docs.python.org/3.12/library/dis.html#opcode-EXTENDED_ARG
    """
    OPCODE_NAME = 'EXTENDED_ARG'
    OPCODE_VALUE = 144

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(EXTENDED_ARG) {
        #     assert(oparg);
        #     assert(cframe.use_tracing == 0);
        #     opcode = _Py_OPCODE(*next_instr);
        #     oparg = oparg << 8 | _Py_OPARG(*next_instr);
        #     PRE_DISPATCH_GOTO();
        #     DISPATCH_GOTO();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
