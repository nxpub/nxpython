# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreAttrInstanceValue(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_ATTR_INSTANCE_VALUE'
    value = 154

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_ATTR_INSTANCE_VALUE, (unused/1, type_version/2, index/1, value, owner --)) {
        #     assert(cframe.use_tracing == 0);
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, STORE_ATTR);
        #     assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT);
        #     PyDictOrValues dorv = *_PyObject_DictOrValuesPointer(owner);
        #     DEOPT_IF(!_PyDictOrValues_IsValues(dorv), STORE_ATTR);
        #     STAT_INC(STORE_ATTR, hit);
        #     PyDictValues *values = _PyDictOrValues_GetValues(dorv);
        #     PyObject *old_value = values->values[index];
        #     values->values[index] = value;
        #     if (old_value == NULL) {
        #         _PyDictValues_AddToInsertionOrder(values, index);
        #     }
        #     else {
        #         Py_DECREF(old_value);
        #     }
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
        # assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT)
        dorv = *_PyObject_DictOrValuesPointer(owner)
        cls.flow.deopt_if(not cls.api.private.PyDictOrValues_IsValues(dorv), 'STORE_ATTR')
        cls.flow.stat_inc('STORE_ATTR', 'hit')
        values = cls.api.private.PyDictOrValues_GetValues(dorv)
        old_value = values.values[index]
        values.values[index] = value
        if old_value == None:
            cls.api.private.PyDictValues_AddToInsertionOrder(values, index)
        else:
            cls.memory.dec_ref(old_value)
        cls.memory.dec_ref(owner)
        cls.stack.shrink(2)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
