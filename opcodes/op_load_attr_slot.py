# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrSlot(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_SLOT'
    value = 77

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_SLOT) {
        #     assert(cframe.use_tracing == 0);
        #     PyObject *owner = TOP();
        #     PyObject *res;
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     uint32_t type_version = read_u32(cache->version);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, LOAD_ATTR);
        #     char *addr = (char *)owner + cache->index;
        #     res = *(PyObject **)addr;
        #     DEOPT_IF(res == NULL, LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);
        #     Py_INCREF(res);
        #     SET_TOP(NULL);
        #     STACK_GROW((oparg & 1));
        #     SET_TOP(res);
        #     Py_DECREF(owner);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        # }
        # assert(cframe.use_tracing == 0)
        owner = cls.stack.top()
        tp = cls.api.Py_TYPE(owner)
