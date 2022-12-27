# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinarySubscrListInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_SUBSCR_LIST_INT'
    OPCODE_VALUE = 20

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, list, sub) -> None:
        # TARGET(BINARY_SUBSCR_LIST_INT) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *list = PEEK(2);
        #     PyObject *res;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(sub), BINARY_SUBSCR);
        #     DEOPT_IF(!PyList_CheckExact(list), BINARY_SUBSCR);

        #     // Deopt unless 0 <= sub < PyList_Size(list)
        #     DEOPT_IF(!_PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR);
        #     assert(((PyLongObject *)_PyLong_GetZero())->ob_digit[0] == 0);
        #     Py_ssize_t index = ((PyLongObject*)sub)->ob_digit[0];
        #     DEOPT_IF(index >= PyList_GET_SIZE(list), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     res = PyList_GET_ITEM(list, index);
        #     assert(res != NULL);
        #     Py_INCREF(res);
        #     _Py_DECREF_SPECIALIZED(sub, (destructor)PyObject_Free);
        #     Py_DECREF(list);
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
