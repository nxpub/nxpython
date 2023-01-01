# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreAttrSlot(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_ATTR_SLOT'
    value = 158

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_ATTR_SLOT, (unused/1, type_version/2, index/1, value, owner --)) {
        #     assert(cframe.use_tracing == 0);
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, STORE_ATTR);
        #     char *addr = (char *)owner + index;
        #     STAT_INC(STORE_ATTR, hit);
        #     PyObject *old_value = *(PyObject **)addr;
        #     *(PyObject **)addr = value;
        #     Py_XDECREF(old_value);
        #     Py_DECREF(owner);
        # }
        owner = cls.stack.peek(1)
        value = cls.stack.peek(2)
        type_version = read_u32(next_instr[1].cache)
        index = read_u16(next_instr[3].cache)
        # assert(cframe.use_tracing == 0)
        tp = cls.api.Py_TYPE(owner)
        # assert(type_version != 0)
        cls.flow.deopt_if(tp.tp_version_tag != type_version, 'STORE_ATTR')
        addr = owner + index
        cls.flow.stat_inc('STORE_ATTR', 'hit')
        old_value = *(*)addr
        *(*)addr = value
        cls.memory.dec_ref_x(old_value)
        cls.memory.dec_ref(owner)
        cls.stack.shrink(2)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
