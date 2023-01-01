# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreAttrWithHint(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_ATTR_WITH_HINT'
    value = 159

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_ATTR_WITH_HINT, (unused/1, type_version/2, hint/1, value, owner --)) {
        #     assert(cframe.use_tracing == 0);
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, STORE_ATTR);
        #     assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT);
        #     PyDictOrValues dorv = *_PyObject_DictOrValuesPointer(owner);
        #     DEOPT_IF(_PyDictOrValues_IsValues(dorv), STORE_ATTR);
        #     PyDictObject *dict = (PyDictObject *)_PyDictOrValues_GetDict(dorv);
        #     DEOPT_IF(dict == NULL, STORE_ATTR);
        #     assert(PyDict_CheckExact((PyObject *)dict));
        #     PyObject *name = GETITEM(names, oparg);
        #     DEOPT_IF(hint >= (size_t)dict->ma_keys->dk_nentries, STORE_ATTR);
        #     PyObject *old_value;
        #     uint64_t new_version;
        #     if (DK_IS_UNICODE(dict->ma_keys)) {
        #         PyDictUnicodeEntry *ep = DK_UNICODE_ENTRIES(dict->ma_keys) + hint;
        #         DEOPT_IF(ep->me_key != name, STORE_ATTR);
        #         old_value = ep->me_value;
        #         DEOPT_IF(old_value == NULL, STORE_ATTR);
        #         new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value);
        #         ep->me_value = value;
        #     }
        #     else {
        #         PyDictKeyEntry *ep = DK_ENTRIES(dict->ma_keys) + hint;
        #         DEOPT_IF(ep->me_key != name, STORE_ATTR);
        #         old_value = ep->me_value;
        #         DEOPT_IF(old_value == NULL, STORE_ATTR);
        #         new_version = _PyDict_NotifyEvent(PyDict_EVENT_MODIFIED, dict, name, value);
        #         ep->me_value = value;
        #     }
        #     Py_DECREF(old_value);
        #     STAT_INC(STORE_ATTR, hit);
        #     /* Ensure dict is GC tracked if it needs to be */
        #     if (!_PyObject_GC_IS_TRACKED(dict) && _PyObject_GC_MAY_BE_TRACKED(value)) {
        #         _PyObject_GC_TRACK(dict);
        #     }
        #     /* PEP 509 */
        #     dict->ma_version_tag = new_version;
        #     Py_DECREF(owner);
        # }
        owner = cls.stack.peek(1)
        value = cls.stack.peek(2)
        type_version = read_u32(next_instr[1].cache)
        hint = read_u16(next_instr[3].cache)
        # assert(cframe.use_tracing == 0)
        tp = cls.api.Py_TYPE(owner)
        # assert(type_version != 0)
        cls.flow.deopt_if(tp.tp_version_tag != type_version, 'STORE_ATTR')
        # assert(tp->tp_flags & Py_TPFLAGS_MANAGED_DICT)
        dorv = *_PyObject_DictOrValuesPointer(owner)
        cls.flow.deopt_if(cls.api.private.PyDictOrValues_IsValues(dorv), 'STORE_ATTR')
        dict = cls.api.private.PyDictOrValues_GetDict(dorv)
        cls.flow.deopt_if(dict == None, 'STORE_ATTR')
        # assert(PyDict_CheckExact((PyObject *)dict))
        name = cls.frame.get_name(oparg)
        cls.flow.deopt_if(hint >= (size_t)dict.ma_keys.dk_nentries, 'STORE_ATTR')
        if DK_IS_UNICODE(dict.ma_keys):
            ep = DK_UNICODE_ENTRIES(dict.ma_keys) + hint
            cls.flow.deopt_if(ep.me_key != name, 'STORE_ATTR')
            old_value = ep.me_value
            cls.flow.deopt_if(old_value == None, 'STORE_ATTR')
            new_version = cls.api.private.PyDict_NotifyEvent(cls.api.PyDict_EVENT_MODIFIED, dict, name, value)
            ep.me_value = value
        else:
            ep = DK_ENTRIES(dict.ma_keys) + hint
            cls.flow.deopt_if(ep.me_key != name, 'STORE_ATTR')
            old_value = ep.me_value
            cls.flow.deopt_if(old_value == None, 'STORE_ATTR')
            new_version = cls.api.private.PyDict_NotifyEvent(cls.api.PyDict_EVENT_MODIFIED, dict, name, value)
            ep.me_value = value
        cls.memory.dec_ref(old_value)
        cls.flow.stat_inc('STORE_ATTR', 'hit')
        # Ensure dict is GC tracked if it needs to be 
        if not cls.api.private.PyObject_GC_IS_TRACKED(dict) and cls.api.private.PyObject_GC_MAY_BE_TRACKED(value):
            cls.api.private.PyObject_GC_TRACK(dict)
        # PEP 509 
        dict.ma_version_tag = new_version
        cls.memory.dec_ref(owner)
        cls.stack.shrink(2)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
