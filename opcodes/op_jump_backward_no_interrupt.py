# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpJumpBackwardNoInterrupt(OpCode):
    """
    Decrements bytecode counter by delta. Does not check for interrupts.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_BACKWARD_NO_INTERRUPT
    """
    OPCODE_NAME = 'JUMP_BACKWARD_NO_INTERRUPT'
    OPCODE_VALUE = 134

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(JUMP_BACKWARD_NO_INTERRUPT) {
        #     /* This bytecode is used in the `yield from` or `await` loop.
        #      * If there is an interrupt, we want it handled in the innermost
        #      * generator or coroutine, so we deliberately do not check it here.
        #      * (see bpo-30039).
        #      */
        #     JUMPBY(-oparg);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
