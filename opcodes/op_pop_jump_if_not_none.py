# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPopJumpIfNotNone(OpCode):
    """
    If TOS is not None, increments the bytecode counter by delta.  TOS is popped.
    
    New in version 3.11.
    
    Changed in version 3.12: This is no longer a pseudo-instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_JUMP_IF_NOT_NONE
    """
    OPCODE_NAME = 'POP_JUMP_IF_NOT_NONE'
    OPCODE_VALUE = 128

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(POP_JUMP_IF_NOT_NONE) {
        #     PyObject *value = POP();
        #     if (!Py_IsNone(value)) {
        #         JUMPBY(oparg);
        #     }
        #     Py_DECREF(value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
