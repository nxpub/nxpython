# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBinaryOpAddUnicode(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_ADD_UNICODE'
    OPCODE_VALUE = 7

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(BINARY_OP_ADD_UNICODE) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *res;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyUnicode_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     res = PyUnicode_Concat(left, right);
        #     _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc);
        #     if (res == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
