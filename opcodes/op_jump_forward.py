# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpJumpForward(BaseOpCode):
    """
    Increments bytecode counter by delta.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_FORWARD
    """
    OPCODE_NAME = 'JUMP_FORWARD'
    OPCODE_VALUE = 110

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(JUMP_FORWARD) {
        #     JUMPBY(oparg);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
