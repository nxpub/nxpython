# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreAttr(OpCode):
    """
    Implements TOS.name = TOS1, where namei is the index of name in
    co_names.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_ATTR
    """
    OPCODE_NAME = 'STORE_ATTR'
    OPCODE_VALUE = 95

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, counter, unused, v, owner) -> None:
        # TARGET(STORE_ATTR) {
        #     PREDICTED(STORE_ATTR);
        #     PyObject *owner = PEEK(1);
        #     PyObject *v = PEEK(2);
        #     uint16_t counter = read_u16(&next_instr[0].cache);
        #     if (ADAPTIVE_COUNTER_IS_ZERO(counter)) {
        #         assert(cframe.use_tracing == 0);
        #         PyObject *name = GETITEM(names, oparg);
        #         next_instr--;
        #         _Py_Specialize_StoreAttr(owner, next_instr, name);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(STORE_ATTR, deferred);
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyObject_SetAttr(owner, name, v);
        #     Py_DECREF(v);
        #     Py_DECREF(owner);
        #     if (err) goto pop_2_error;
        #     STACK_SHRINK(2);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
