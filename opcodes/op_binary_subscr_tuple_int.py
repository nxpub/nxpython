# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinarySubscrTupleInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_SUBSCR_TUPLE_INT'
    OPCODE_VALUE = 21

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, tuple, sub) -> None:
        # TARGET(BINARY_SUBSCR_TUPLE_INT) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *tuple = PEEK(2);
        #     PyObject *res;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(sub), BINARY_SUBSCR);
        #     DEOPT_IF(!PyTuple_CheckExact(tuple), BINARY_SUBSCR);

        #     // Deopt unless 0 <= sub < PyTuple_Size(list)
        #     Py_ssize_t signed_magnitude = Py_SIZE(sub);
        #     DEOPT_IF(((size_t)signed_magnitude) > 1, BINARY_SUBSCR);
        #     assert(((PyLongObject *)_PyLong_GetZero())->ob_digit[0] == 0);
        #     Py_ssize_t index = ((PyLongObject*)sub)->ob_digit[0];
        #     DEOPT_IF(index >= PyTuple_GET_SIZE(tuple), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     res = PyTuple_GET_ITEM(tuple, index);
        #     assert(res != NULL);
        #     Py_INCREF(res);
        #     _Py_DECREF_SPECIALIZED(sub, (destructor)PyObject_Free);
        #     Py_DECREF(tuple);
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
