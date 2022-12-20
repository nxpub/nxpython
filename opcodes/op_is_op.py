# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpIsOp(BaseOpCode):
    """
    Performs is comparison, or is not if invert is 1.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-IS_OP
    """
    OPCODE_NAME = 'IS_OP'
    OPCODE_VALUE = 117

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(IS_OP) {
        #     PyObject *right = POP();
        #     PyObject *left = TOP();
        #     int res = Py_Is(left, right) ^ oparg;
        #     PyObject *b = res ? Py_True : Py_False;
        #     SET_TOP(Py_NewRef(b));
        #     Py_DECREF(left);
        #     Py_DECREF(right);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
