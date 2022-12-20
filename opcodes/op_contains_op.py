# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpContainsOp(BaseOpCode):
    """
    Performs in comparison, or not in if invert is 1.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-CONTAINS_OP
    """
    OPCODE_NAME = 'CONTAINS_OP'
    OPCODE_VALUE = 118

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CONTAINS_OP) {
        #     PyObject *right = POP();
        #     PyObject *left = POP();
        #     int res = PySequence_Contains(right, left);
        #     Py_DECREF(left);
        #     Py_DECREF(right);
        #     if (res < 0) {
        #         goto error;
        #     }
        #     PyObject *b = (res^oparg) ? Py_True : Py_False;
        #     PUSH(Py_NewRef(b));
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
