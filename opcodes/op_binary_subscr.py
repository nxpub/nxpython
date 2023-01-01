# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinarySubscr(OpCode):
    """
    Implements TOS = TOS1[TOS].

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_SUBSCR
    """
    name = 'BINARY_SUBSCR'
    value = 25

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_SUBSCR, (unused/4, container, sub -- res)) {
        #     _PyBinarySubscrCache *cache = (_PyBinarySubscrCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_BinarySubscr(container, sub, next_instr);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(BINARY_SUBSCR, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     res = PyObject_GetItem(container, sub);
        #     DECREF_INPUTS();
        #     ERROR_IF(res == NULL, error);
        # }
        # static_assert(INLINE_CACHE_ENTRIES_BINARY_SUBSCR == 4, "incorrect cache size")
        sub = cls.stack.peek(1)
        container = cls.stack.peek(2)
        res = cls.api.PyObject_GetItem(container, sub)
        cls.memory.dec_ref(container)
        cls.memory.dec_ref(sub)
        cls.flow.error_if(res == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
