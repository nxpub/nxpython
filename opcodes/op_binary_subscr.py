# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBinarySubscr(BaseOpCode):
    """
    Implements TOS = TOS1[TOS].

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_SUBSCR
    """
    OPCODE_NAME = 'BINARY_SUBSCR'
    OPCODE_VALUE = 25

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, container, sub) -> None:
        # TARGET(BINARY_SUBSCR) {
        #     PREDICTED(BINARY_SUBSCR);
        #     static_assert(INLINE_CACHE_ENTRIES_BINARY_SUBSCR == 4, "incorrect cache size");
        #     PyObject *sub = PEEK(1);
        #     PyObject *container = PEEK(2);
        #     PyObject *res;
        #     _PyBinarySubscrCache *cache = (_PyBinarySubscrCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_BinarySubscr(container, sub, next_instr);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(BINARY_SUBSCR, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     res = PyObject_GetItem(container, sub);
        #     Py_DECREF(container);
        #     Py_DECREF(sub);
        #     if (res == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
