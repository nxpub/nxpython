# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinarySubscrTupleInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_SUBSCR_TUPLE_INT'
    value = 21

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_SUBSCR_TUPLE_INT, (unused/4, tuple, sub -- res)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(sub), BINARY_SUBSCR);
        #     DEOPT_IF(!PyTuple_CheckExact(tuple), BINARY_SUBSCR);

        #     // Deopt unless 0 <= sub < PyTuple_Size(list)
        #     DEOPT_IF(!_PyLong_IsPositiveSingleDigit(sub), BINARY_SUBSCR);
        #     assert(((PyLongObject *)_PyLong_GetZero())->ob_digit[0] == 0);
        #     Py_ssize_t index = ((PyLongObject*)sub)->ob_digit[0];
        #     DEOPT_IF(index >= PyTuple_GET_SIZE(tuple), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     res = PyTuple_GET_ITEM(tuple, index);
        #     assert(res != NULL);
        #     Py_INCREF(res);
        #     _Py_DECREF_SPECIALIZED(sub, (destructor)PyObject_Free);
        #     Py_DECREF(tuple);
        # }
        sub = cls.stack.peek(1)
        tuple = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(sub), 'BINARY_SUBSCR')
        cls.flow.deopt_if(not cls.api.PyTuple_CheckExact(tuple), 'BINARY_SUBSCR')

        # Deopt unless 0 <= sub < cls.api.PyTuple_Size(list)
        cls.flow.deopt_if(not cls.api.private.PyLong_IsPositiveSingleDigit(sub), 'BINARY_SUBSCR')
        # assert(((PyLongObject *)_PyLong_GetZero())->ob_digit[0] == 0)
        index = (sub).ob_digit[0]
        cls.flow.deopt_if(index >= cls.api.PyTuple_GET_SIZE(tuple), 'BINARY_SUBSCR')
        cls.flow.stat_inc('BINARY_SUBSCR', 'hit')
        res = cls.api.PyTuple_GET_ITEM(tuple, index)
        # assert(res != NULL)
        cls.memory.inc_ref(res)
        cls.memory.dec_ref_specialized(sub, cls.api.PyObject_Free)
        cls.memory.dec_ref(tuple)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
