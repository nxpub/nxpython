# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpLoadAttrMethodWithValues(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'LOAD_ATTR_METHOD_WITH_VALUES'
    OPCODE_VALUE = 86

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_ATTR_METHOD_WITH_VALUES) {
        #     /* Cached method object */
        #     assert(cframe.use_tracing == 0);
        #     PyObject *self = TOP();
        #     PyTypeObject *self_cls = Py_TYPE(self);
        #     _PyLoadMethodCache *cache = (_PyLoadMethodCache *)next_instr;
        #     uint32_t type_version = read_u32(cache->type_version);
        #     assert(type_version != 0);
        #     DEOPT_IF(self_cls->tp_version_tag != type_version, LOAD_ATTR);
        #     assert(self_cls->tp_flags & Py_TPFLAGS_MANAGED_DICT);
        #     PyDictOrValues dorv = *_PyObject_DictOrValuesPointer(self);
        #     DEOPT_IF(!_PyDictOrValues_IsValues(dorv), LOAD_ATTR);
        #     PyHeapTypeObject *self_heap_type = (PyHeapTypeObject *)self_cls;
        #     DEOPT_IF(self_heap_type->ht_cached_keys->dk_version !=
        #              read_u32(cache->keys_version), LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);
        #     PyObject *res = read_obj(cache->descr);
        #     assert(res != NULL);
        #     assert(_PyType_HasFeature(Py_TYPE(res), Py_TPFLAGS_METHOD_DESCRIPTOR));
        #     SET_TOP(Py_NewRef(res));
        #     PUSH(self);
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
