# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadAttrInstanceValue(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'LOAD_ATTR_INSTANCE_VALUE'
    OPCODE_VALUE = 72

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_ATTR_INSTANCE_VALUE) {
        #     assert(cframe.use_tracing == 0);
        #     PyObject *owner = TOP();
        #     PyObject *res;
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     uint32_t type_version = read_u32(cache->version);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, LOAD_ATTR);
        #     assert(tp->tp_dictoffset < 0);
        #     assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT);
        #     PyDictOrValues dorv = *_PyObject_DictOrValuesPointer(owner);
        #     DEOPT_IF(!_PyDictOrValues_IsValues(dorv), LOAD_ATTR);
        #     res = _PyDictOrValues_GetValues(dorv)->values[cache->index];
        #     DEOPT_IF(res == NULL, LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);
        #     Py_INCREF(res);
        #     SET_TOP(NULL);
        #     STACK_GROW((oparg & 1));
        #     SET_TOP(res);
        #     Py_DECREF(owner);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
