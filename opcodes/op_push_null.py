# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPushNull(OpCode):
    """
    Pushes a NULL to the stack.
    Used in the call sequence to match the NULL pushed by
    LOAD_METHOD for non-method calls.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-PUSH_NULL
    """
    OPCODE_NAME = 'PUSH_NULL'
    OPCODE_VALUE = 2

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(PUSH_NULL) {
        #     PyObject *res;
        #     res = NULL;
        #     STACK_GROW(1);
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
