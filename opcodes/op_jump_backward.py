# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpJumpBackward(BaseOpCode):
    """
    Decrements bytecode counter by delta. Checks for interrupts.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_BACKWARD
    """
    OPCODE_NAME = 'JUMP_BACKWARD'
    OPCODE_VALUE = 140

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(JUMP_BACKWARD) {
        #     PREDICTED(JUMP_BACKWARD);
        #     assert(oparg < INSTR_OFFSET());
        #     JUMPBY(-oparg);
        #     CHECK_EVAL_BREAKER();
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
