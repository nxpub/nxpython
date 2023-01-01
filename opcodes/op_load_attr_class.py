# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrClass(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_CLASS'
    value = 66

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_CLASS) {
        #     assert(cframe.use_tracing == 0);
        #     _PyLoadMethodCache *cache = (_PyLoadMethodCache *)next_instr;

        #     PyObject *cls = TOP();
        #     DEOPT_IF(!PyType_Check(cls), LOAD_ATTR);
        #     uint32_t type_version = read_u32(cache->type_version);
        #     DEOPT_IF(((PyTypeObject *)cls)->tp_version_tag != type_version,
        #         LOAD_ATTR);
        #     assert(type_version != 0);

        #     STAT_INC(LOAD_ATTR, hit);
        #     PyObject *res = read_obj(cache->descr);
        #     assert(res != NULL);
        #     Py_INCREF(res);
        #     SET_TOP(NULL);
        #     STACK_GROW((oparg & 1));
        #     SET_TOP(res);
        #     Py_DECREF(cls);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        # }
        # assert(cframe.use_tracing == 0)


