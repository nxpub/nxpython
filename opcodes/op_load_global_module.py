# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadGlobalModule(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_GLOBAL_MODULE'
    value = 153

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: LOAD_GLOBAL has irregular stack effect
        # inst(LOAD_GLOBAL_MODULE) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL);
        #     PyDictObject *dict = (PyDictObject *)GLOBALS();
        #     _PyLoadGlobalCache *cache = (_PyLoadGlobalCache *)next_instr;
        #     uint32_t version = read_u32(cache->module_keys_version);
        #     DEOPT_IF(dict->ma_keys->dk_version != version, LOAD_GLOBAL);
        #     assert(DK_IS_UNICODE(dict->ma_keys));
        #     PyDictUnicodeEntry *entries = DK_UNICODE_ENTRIES(dict->ma_keys);
        #     PyObject *res = entries[cache->index].me_value;
        #     DEOPT_IF(res == NULL, LOAD_GLOBAL);
        #     int push_null = oparg & 1;
        #     PEEK(0) = NULL;
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL);
        #     STAT_INC(LOAD_GLOBAL, hit);
        #     STACK_GROW(push_null+1);
        #     SET_TOP(Py_NewRef(res));
        # }
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyDict_CheckExact(cls.frame.get_globals()), 'LOAD_GLOBAL')
        dict = cls.frame.get_globals()
