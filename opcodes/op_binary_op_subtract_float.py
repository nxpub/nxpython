# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinaryOpSubtractFloat(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_SUBTRACT_FLOAT'
    OPCODE_VALUE = 16

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(BINARY_OP_SUBTRACT_FLOAT) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *sub;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyFloat_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyFloat_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     double dsub = ((PyFloatObject *)left)->ob_fval - ((PyFloatObject *)right)->ob_fval;
        #     sub = PyFloat_FromDouble(dsub);
        #     _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc);
        #     if (sub == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, sub);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
