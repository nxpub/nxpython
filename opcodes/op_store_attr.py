# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreAttr(OpCode):
    """
    Implements TOS.name = TOS1, where namei is the index of name in
    co_names.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_ATTR
    """
    name = 'STORE_ATTR'
    value = 95

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_ATTR, (counter/1, unused/3, v, owner --)) {
        #     if (ADAPTIVE_COUNTER_IS_ZERO(counter)) {
        #         assert(cframe.use_tracing == 0);
        #         PyObject *name = GETITEM(names, oparg);
        #         next_instr--;
        #         _Py_Specialize_StoreAttr(owner, next_instr, name);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(STORE_ATTR, deferred);
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyObject_SetAttr(owner, name, v);
        #     Py_DECREF(v);
        #     Py_DECREF(owner);
        #     ERROR_IF(err, error);
        # }
        owner = cls.stack.peek(1)
        v = cls.stack.peek(2)
        counter = read_u16(next_instr[0].cache)
        if ADAPTIVE_COUNTER_IS_ZERO(counter):
            # assert(cframe.use_tracing == 0)
            name = cls.frame.get_name(oparg)
            next_instr--
            cls.api.private.Py_Specialize_StoreAttr(owner, next_instr, name)
            DISPATCH_SAME_OPARG()
        cls.flow.stat_inc('STORE_ATTR', 'deferred')
        name = cls.frame.get_name(oparg)
        err = cls.api.PyObject_SetAttr(owner, name, v)
        cls.memory.dec_ref(v)
        cls.memory.dec_ref(owner)
        cls.flow.error_if(err, 2)
        cls.stack.shrink(2)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
