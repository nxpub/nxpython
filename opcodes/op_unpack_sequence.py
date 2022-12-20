# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpUnpackSequence(BaseOpCode):
    """
    Unpacks TOS into count individual values, which are put onto the stack
    right-to-left.

    https://docs.python.org/3.12/library/dis.html#opcode-UNPACK_SEQUENCE
    """
    OPCODE_NAME = 'UNPACK_SEQUENCE'
    OPCODE_VALUE = 92

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(UNPACK_SEQUENCE) {
        #     PREDICTED(UNPACK_SEQUENCE);
        #     _PyUnpackSequenceCache *cache = (_PyUnpackSequenceCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         PyObject *seq = TOP();
        #         next_instr--;
        #         _Py_Specialize_UnpackSequence(seq, next_instr, oparg);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(UNPACK_SEQUENCE, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     PyObject *seq = POP();
        #     PyObject **top = stack_pointer + oparg;
        #     if (!unpack_iterable(tstate, seq, oparg, -1, top)) {
        #         Py_DECREF(seq);
        #         goto error;
        #     }
        #     STACK_GROW(oparg);
        #     Py_DECREF(seq);
        #     JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
