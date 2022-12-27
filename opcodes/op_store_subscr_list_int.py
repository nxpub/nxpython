# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreSubscrListInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_SUBSCR_LIST_INT'
    OPCODE_VALUE = 167

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, value, list, sub) -> None:
        # TARGET(STORE_SUBSCR_LIST_INT) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *list = PEEK(2);
        #     PyObject *value = PEEK(3);
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(sub), STORE_SUBSCR);
        #     DEOPT_IF(!PyList_CheckExact(list), STORE_SUBSCR);

        #     // Ensure nonnegative, zero-or-one-digit ints.
        #     DEOPT_IF(!_PyLong_IsPositiveSingleDigit(sub), STORE_SUBSCR);
        #     Py_ssize_t index = ((PyLongObject*)sub)->ob_digit[0];
        #     // Ensure index < len(list)
        #     DEOPT_IF(index >= PyList_GET_SIZE(list), STORE_SUBSCR);
        #     STAT_INC(STORE_SUBSCR, hit);

        #     PyObject *old_value = PyList_GET_ITEM(list, index);
        #     PyList_SET_ITEM(list, index, value);
        #     assert(old_value != NULL);
        #     Py_DECREF(old_value);
        #     _Py_DECREF_SPECIALIZED(sub, (destructor)PyObject_Free);
        #     Py_DECREF(list);
        #     STACK_SHRINK(3);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
