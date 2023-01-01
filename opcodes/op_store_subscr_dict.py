# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreSubscrDict(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_SUBSCR_DICT'
    value = 166

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_SUBSCR_DICT, (unused/1, value, dict, sub -- )) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(dict), STORE_SUBSCR);
        #     STAT_INC(STORE_SUBSCR, hit);
        #     int err = _PyDict_SetItem_Take2((PyDictObject *)dict, sub, value);
        #     Py_DECREF(dict);
        #     ERROR_IF(err, error);
        # }
        sub = cls.stack.peek(1)
        dict = cls.stack.peek(2)
        value = cls.stack.peek(3)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyDict_CheckExact(dict), 'STORE_SUBSCR')
        cls.flow.stat_inc('STORE_SUBSCR', 'hit')
        err = cls.api.private.PyDict_SetItem_Take2(dict, sub, value)
        cls.memory.dec_ref(dict)
        cls.flow.error_if(err, 3)
        cls.stack.shrink(3)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
