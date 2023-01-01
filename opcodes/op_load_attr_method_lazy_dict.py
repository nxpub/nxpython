# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrMethodLazyDict(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_METHOD_LAZY_DICT'
    value = 79

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_METHOD_LAZY_DICT) {
        #     assert(cframe.use_tracing == 0);
        #     PyObject *self = TOP();
        #     PyTypeObject *self_cls = Py_TYPE(self);
        #     _PyLoadMethodCache *cache = (_PyLoadMethodCache *)next_instr;
        #     uint32_t type_version = read_u32(cache->type_version);
        #     DEOPT_IF(self_cls->tp_version_tag != type_version, LOAD_ATTR);
        #     Py_ssize_t dictoffset = self_cls->tp_dictoffset;
        #     assert(dictoffset > 0);
        #     PyObject *dict = *(PyObject **)((char *)self + dictoffset);
        #     /* This object has a __dict__, just not yet created */
        #     DEOPT_IF(dict != NULL, LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);
        #     PyObject *res = read_obj(cache->descr);
        #     assert(res != NULL);
        #     assert(_PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR));
        #     SET_TOP(Py_NewRef(res));
        #     PUSH(self);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        # }
        # assert(cframe.use_tracing == 0)
        self = cls.stack.top()
        self_cls = cls.api.Py_TYPE(self)
        # This object has a __dict__, just not yet created 
