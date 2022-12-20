import os
import sys
import json
import logging
import sys
import hashlib

from pathlib import Path
from git import Repo

from cases_generator.generate_opcodes import DSLAnalyzer

CPYTHON_GIT_URL = 'https://github.com/python/cpython.git'
CPYTHON_LOCAL_PATH = './build/cpython'
STATE_PATH = './state.json'

# TODO: Is there a way to avoid patching w/ sys.path?
CASES_GENERATOR_FILES = {
    './Tools/cases_generator/generate_cases.py': {
        'import parser': 'from cases_generator import parser',
        'from parser import StackEffect': 'from cases_generator.parser import StackEffect',
    },
    './Tools/cases_generator/lexer.py': {
        # N/A
    },
    './Tools/cases_generator/parser.py': {
        'import lexer as lx': 'import cases_generator.lexer as lx',
        'from plexer import PLexer': 'from cases_generator.plexer import PLexer',
    },
    './Tools/cases_generator/plexer.py': {
        'import lexer as lx': 'import cases_generator.lexer as lx',
    },
}

BYTECODES_FILE = './Python/bytecodes.c'


# TODO: Get rid of the submodule
def start_session() -> dict:
    # Load previous state
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as state_file:
            state = json.loads(state_file.read())
    else:
        state = {'sha': None}

    if not os.path.exists(CPYTHON_LOCAL_PATH):
        print('cloning...')
        repo = Repo.clone_from(CPYTHON_GIT_URL, CPYTHON_LOCAL_PATH)
        print('cloned!')
    else:
        print('pulling...')
        repo = Repo(CPYTHON_LOCAL_PATH)
        repo.remote('origin').pull()
        print('pulled')

    current_sha = repo.head.commit.hexsha
    print('sha', current_sha)

    # TODO: Copy CASES_GENERATOR_FILES from cpython distribution locally, verify checksums

    # Render all the opcodes, compare with the previous session
    analyzer = DSLAnalyzer(
        dsl_path=str(Path(CPYTHON_LOCAL_PATH) / Path(BYTECODES_FILE)),
        output_path='./opcodes/',
        opcode_h_path=str(Path(CPYTHON_LOCAL_PATH) / Path('Include/opcode.h')),
        cpython_sha=current_sha,
    )
    analyzer.parse()
    analyzer.analyze()
    if analyzer.errors:
        sys.exit(f'Found {analyzer.errors} errors')
    analyzer.write_instructions()

    # Track changes in the list of files


def end_session():
    # Save current state
    with open(STATE_PATH, 'w') as state_file:
        state_file.write(json.dumps(state))


def run(args: list[str] | None = None):
    if not args:
        args = sys.argv[1:]
    match cmd := args[0]:
        case 'start':
            start_session()
        case 'end':
            end_session()
        case _:
            raise NotImplementedError(f'Unknown command {cmd}')


if __name__ == '__main__':
    run(['start'])
