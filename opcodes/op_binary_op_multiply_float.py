# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBinaryOpMultiplyFloat(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_MULTIPLY_FLOAT'
    OPCODE_VALUE = 13

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(BINARY_OP_MULTIPLY_FLOAT) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *prod;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyFloat_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyFloat_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     double dprod = ((PyFloatObject *)left)->ob_fval *
        #         ((PyFloatObject *)right)->ob_fval;
        #     prod = PyFloat_FromDouble(dprod);
        #     _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc);
        #     if (prod == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, prod);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError