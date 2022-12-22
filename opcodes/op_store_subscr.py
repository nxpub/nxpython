# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreSubscr(OpCode):
    """
    Implements TOS1[TOS] = TOS2.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_SUBSCR
    """
    OPCODE_NAME = 'STORE_SUBSCR'
    OPCODE_VALUE = 60

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, counter, v, container, sub) -> None:
        # TARGET(STORE_SUBSCR) {
        #     PREDICTED(STORE_SUBSCR);
        #     PyObject *sub = PEEK(1);
        #     PyObject *container = PEEK(2);
        #     PyObject *v = PEEK(3);
        #     uint16_t counter = read_u16(&next_instr[0].cache);
        #     if (ADAPTIVE_COUNTER_IS_ZERO(counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_StoreSubscr(container, sub, next_instr);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(STORE_SUBSCR, deferred);
        #     _PyStoreSubscrCache *cache = (_PyStoreSubscrCache *)next_instr;
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     /* container[sub] = v */
        #     int err = PyObject_SetItem(container, sub, v);
        #     Py_DECREF(v);
        #     Py_DECREF(container);
        #     Py_DECREF(sub);
        #     if (err) goto pop_3_error;
        #     STACK_SHRINK(3);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
