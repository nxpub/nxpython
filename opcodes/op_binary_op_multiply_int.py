# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinaryOpMultiplyInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_MULTIPLY_INT'
    OPCODE_VALUE = 14

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(BINARY_OP_MULTIPLY_INT) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *prod;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyLong_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     prod = _PyLong_Multiply((PyLongObject *)left, (PyLongObject *)right);
        #     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #     if (prod == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, prod);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
