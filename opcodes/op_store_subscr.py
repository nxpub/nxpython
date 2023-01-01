# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreSubscr(OpCode):
    """
    Implements TOS1[TOS] = TOS2.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_SUBSCR
    """
    name = 'STORE_SUBSCR'
    value = 60

    @classmethod
    def logic(cls) -> None:
        # inst(STORE_SUBSCR, (counter/1, v, container, sub -- )) {
        #     if (ADAPTIVE_COUNTER_IS_ZERO(counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_StoreSubscr(container, sub, next_instr);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(STORE_SUBSCR, deferred);
        #     _PyStoreSubscrCache *cache = (_PyStoreSubscrCache *)next_instr;
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     /* container[sub] = v */
        #     int err = PyObject_SetItem(container, sub, v);
        #     DECREF_INPUTS();
        #     ERROR_IF(err, error);
        # }
        sub = cls.stack.peek(1)
        container = cls.stack.peek(2)
        v = cls.stack.peek(3)
        counter = read_u16(next_instr[0].cache)
        if ADAPTIVE_COUNTER_IS_ZERO(counter):
            # assert(cframe.use_tracing == 0)
            next_instr--
            cls.api.private.Py_Specialize_StoreSubscr(container, sub, next_instr)
            DISPATCH_SAME_OPARG()
        cls.flow.stat_inc('STORE_SUBSCR', 'deferred')
        # container[sub] = v 
        err = cls.api.PyObject_SetItem(container, sub, v)
        cls.memory.dec_ref(v)
        cls.memory.dec_ref(container)
        cls.memory.dec_ref(sub)
        cls.flow.error_if(err, 3)
        cls.stack.shrink(3)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
