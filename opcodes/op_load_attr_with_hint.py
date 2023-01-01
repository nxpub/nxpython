# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrWithHint(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_WITH_HINT'
    value = 78

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_WITH_HINT) {
        #     assert(cframe.use_tracing == 0);
        #     PyObject *owner = TOP();
        #     PyObject *res;
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     uint32_t type_version = read_u32(cache->version);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, LOAD_ATTR);
        #     assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT);
        #     PyDictOrValues dorv = *_PyObject_DictOrValuesPointer(owner);
        #     DEOPT_IF(_PyDictOrValues_IsValues(dorv), LOAD_ATTR);
        #     PyDictObject *dict = (PyDictObject *)_PyDictOrValues_GetDict(dorv);
        #     DEOPT_IF(dict == NULL, LOAD_ATTR);
        #     assert(PyDict_CheckExact((PyObject *)dict));
        #     PyObject *name = GETITEM(names, oparg>>1);
        #     uint16_t hint = cache->index;
        #     DEOPT_IF(hint >= (size_t)dict->ma_keys->dk_nentries, LOAD_ATTR);
        #     if (DK_IS_UNICODE(dict->ma_keys)) {
        #         PyDictUnicodeEntry *ep = DK_UNICODE_ENTRIES(dict->ma_keys) + hint;
        #         DEOPT_IF(ep->me_key != name, LOAD_ATTR);
        #         res = ep->me_value;
        #     }
        #     else {
        #         PyDictKeyEntry *ep = DK_ENTRIES(dict->ma_keys) + hint;
        #         DEOPT_IF(ep->me_key != name, LOAD_ATTR);
        #         res = ep->me_value;
        #     }
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
