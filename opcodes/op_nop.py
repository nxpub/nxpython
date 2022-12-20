# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpNop(BaseOpCode):
    """
    Do nothing code.  Used as a placeholder by the bytecode optimizer, and to
    generate line tracing events.

    https://docs.python.org/3.12/library/dis.html#opcode-NOP
    """
    OPCODE_NAME = 'NOP'
    OPCODE_VALUE = 9

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(NOP) {
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
