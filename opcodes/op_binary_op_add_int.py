# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinaryOpAddInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_ADD_INT'
    OPCODE_VALUE = 6

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(BINARY_OP_ADD_INT) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *sum;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     sum = _PyLong_Add((PyLongObject *)left, (PyLongObject *)right);
        #     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #     if (sum == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, sum);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
