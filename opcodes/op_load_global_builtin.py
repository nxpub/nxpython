# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadGlobalBuiltin(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_GLOBAL_BUILTIN'
    value = 143

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: LOAD_GLOBAL has irregular stack effect
        # inst(LOAD_GLOBAL_BUILTIN) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(GLOBALS()), LOAD_GLOBAL);
        #     DEOPT_IF(!PyDict_CheckExact(BUILTINS()), LOAD_GLOBAL);
        #     PyDictObject *mdict = (PyDictObject *)GLOBALS();
        #     PyDictObject *bdict = (PyDictObject *)BUILTINS();
        #     _PyLoadGlobalCache *cache = (_PyLoadGlobalCache *)next_instr;
        #     uint32_t mod_version = read_u32(cache->module_keys_version);
        #     uint16_t bltn_version = cache->builtin_keys_version;
        #     DEOPT_IF(mdict->ma_keys->dk_version != mod_version, LOAD_GLOBAL);
        #     DEOPT_IF(bdict->ma_keys->dk_version != bltn_version, LOAD_GLOBAL);
        #     assert(DK_IS_UNICODE(bdict->ma_keys));
        #     PyDictUnicodeEntry *entries = DK_UNICODE_ENTRIES(bdict->ma_keys);
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
        cls.flow.deopt_if(not cls.api.PyDict_CheckExact(cls.frame.get_builtins()), 'LOAD_GLOBAL')
        mdict = cls.frame.get_globals()
        bdict = cls.frame.get_builtins()
