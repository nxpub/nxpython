# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPopTop(OpCode):
    """
    Removes the top-of-stack (TOS) item.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_TOP
    """
    OPCODE_NAME = 'POP_TOP'
    OPCODE_VALUE = 1

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(POP_TOP) {
        #     PyObject *value = PEEK(1);
        #     Py_DECREF(value);
        #     STACK_SHRINK(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
