# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpUnaryInvert(BaseOpCode):
    """
    Implements TOS = ~TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_INVERT
    """
    OPCODE_NAME = 'UNARY_INVERT'
    OPCODE_VALUE = 15

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(UNARY_INVERT) {
        #     PyObject *value = PEEK(1);
        #     PyObject *res;
        #     res = PyNumber_Invert(value);
        #     Py_DECREF(value);
        #     if (res == NULL) goto pop_1_error;
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
