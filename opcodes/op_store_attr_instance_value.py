# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreAttrInstanceValue(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_ATTR_INSTANCE_VALUE'
    OPCODE_VALUE = 154

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, type_version, index, value, owner) -> None:
        # TARGET(STORE_ATTR_INSTANCE_VALUE) {
        #     PyObject *owner = PEEK(1);
        #     PyObject *value = PEEK(2);
        #     uint32_t type_version = read_u32(&next_instr[1].cache);
        #     uint16_t index = read_u16(&next_instr[3].cache);
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
        #     STACK_SHRINK(2);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
