# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpUnaryNot(BaseOpCode):
    """
    Implements TOS = not TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_NOT
    """
    OPCODE_NAME = 'UNARY_NOT'
    OPCODE_VALUE = 12

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(UNARY_NOT) {
        #     PyObject *value = PEEK(1);
        #     PyObject *res;
        #     int err = PyObject_IsTrue(value);
        #     Py_DECREF(value);
        #     if (err < 0) goto pop_1_error;
        #     if (err == 0) {
        #         res = Py_True;
        #     }
        #     else {
        #         res = Py_False;
        #     }
        #     Py_INCREF(res);
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
