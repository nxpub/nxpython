# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrModule(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_MODULE'
    value = 73

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_MODULE) {
        #     assert(cframe.use_tracing == 0);
        #     PyObject *owner = TOP();
        #     PyObject *res;
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     DEOPT_IF(!PyModule_CheckExact(owner), LOAD_ATTR);
        #     PyDictObject *dict = (PyDictObject *)((PyModuleObject *)owner)->md_dict;
        #     assert(dict != NULL);
        #     DEOPT_IF(dict->ma_keys->dk_version != read_u32(cache->version),
        #         LOAD_ATTR);
        #     assert(dict->ma_keys->dk_kind == DICT_KEYS_UNICODE);
        #     assert(cache->index < dict->ma_keys->dk_nentries);
        #     PyDictUnicodeEntry *ep = DK_UNICODE_ENTRIES(dict->ma_keys) + cache->index;
        #     res = ep->me_value;
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
