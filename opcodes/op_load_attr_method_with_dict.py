# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrMethodWithDict(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_METHOD_WITH_DICT'
    value = 81

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_METHOD_WITH_DICT) {
        #     /* Can be either a managed dict, or a tp_dictoffset offset.*/
        #     assert(cframe.use_tracing == 0);
        #     PyObject *self = TOP();
        #     PyTypeObject *self_cls = Py_TYPE(self);
        #     _PyLoadMethodCache *cache = (_PyLoadMethodCache *)next_instr;

        #     DEOPT_IF(self_cls->tp_version_tag != read_u32(cache->type_version),
        #              LOAD_ATTR);
        #     /* Treat index as a signed 16 bit value */
        #     Py_ssize_t dictoffset = self_cls->tp_dictoffset;
        #     assert(dictoffset > 0);
        #     PyDictObject **dictptr = (PyDictObject**)(((char *)self)+dictoffset);
        #     PyDictObject *dict = *dictptr;
        #     DEOPT_IF(dict == NULL, LOAD_ATTR);
        #     DEOPT_IF(dict->ma_keys->dk_version != read_u32(cache->keys_version),
        #              LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);
        #     PyObject *res = read_obj(cache->descr);
        #     assert(res != NULL);
        #     assert(_PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR));
        #     SET_TOP(Py_NewRef(res));
        #     PUSH(self);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        # }
        # Can be either a managed dict, or a tp_dictoffset offset.
        # assert(cframe.use_tracing == 0)
        self = cls.stack.top()
        self_cls = cls.api.Py_TYPE(self)

        # Treat index as a signed 16 bit value 
