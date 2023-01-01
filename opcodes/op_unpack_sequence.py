# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnpackSequence(OpCode):
    """
    Unpacks TOS into count individual values, which are put onto the stack
    right-to-left.

    https://docs.python.org/3.12/library/dis.html#opcode-UNPACK_SEQUENCE
    """
    name = 'UNPACK_SEQUENCE'
    value = 92

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- __array[oparg])
        # inst(UNPACK_SEQUENCE) {
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
        # }
        seq = cls.stack.pop()
        top = cls.stack + oparg
        if not unpack_iterable(cls.frame.state, seq, oparg, -1, top):
            cls.memory.dec_ref(seq)
            cls.flow.error()
        cls.stack.grow(oparg)
        cls.memory.dec_ref(seq)
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        cls.flow.dispatch()
