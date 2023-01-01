# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreSubscrListInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_SUBSCR_LIST_INT'
    value = 167

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_SUBSCR_LIST_INT, (unused/1, value, list, sub -- )) {
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
        # }
        sub = cls.stack.peek(1)
        list = cls.stack.peek(2)
        value = cls.stack.peek(3)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(sub), 'STORE_SUBSCR')
        cls.flow.deopt_if(not cls.api.PyList_CheckExact(list), 'STORE_SUBSCR')

        # Ensure nonnegative, zero-or-one-digit ints.
        cls.flow.deopt_if(not cls.api.private.PyLong_IsPositiveSingleDigit(sub), 'STORE_SUBSCR')
        index = (sub).ob_digit[0]
        # Ensure index < len(list)
        cls.flow.deopt_if(index >= cls.api.PyList_GET_SIZE(list), 'STORE_SUBSCR')
        cls.flow.stat_inc('STORE_SUBSCR', 'hit')

        old_value = cls.api.PyList_GET_ITEM(list, index)
        cls.api.PyList_SET_ITEM(list, index, value)
        # assert(old_value != NULL)
        cls.memory.dec_ref(old_value)
        cls.memory.dec_ref_specialized(sub, cls.api.PyObject_Free)
        cls.memory.dec_ref(list)
        cls.stack.shrink(3)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
