# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpUnaryPositive(OpCode):
    """
    Implements TOS = +TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_POSITIVE
    """
    OPCODE_NAME = 'UNARY_POSITIVE'
    OPCODE_VALUE = 10

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(UNARY_POSITIVE) {
        #     PyObject *value = PEEK(1);
        #     PyObject *res;
        #     res = PyNumber_Positive(value);
        #     Py_DECREF(value);
        #     if (res == NULL) goto pop_1_error;
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
