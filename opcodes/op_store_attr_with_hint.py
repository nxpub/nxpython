# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreAttrWithHint(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_ATTR_WITH_HINT'
    OPCODE_VALUE = 159

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, type_version, hint, value, owner) -> None:
        # TARGET(STORE_ATTR_WITH_HINT) {
        #     PyObject *owner = PEEK(1);
        #     PyObject *value = PEEK(2);
        #     uint32_t type_version = read_u32(&next_instr[1].cache);
        #     uint16_t hint = read_u16(&next_instr[3].cache);
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
        #     STACK_SHRINK(2);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
