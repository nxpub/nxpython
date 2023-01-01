# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnpackSequenceTuple(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'UNPACK_SEQUENCE_TUPLE'
    value = 169

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- __array[oparg])
        # inst(UNPACK_SEQUENCE_TUPLE) {
        #     PyObject *seq = TOP();
        #     DEOPT_IF(!PyTuple_CheckExact(seq), UNPACK_SEQUENCE);
        #     DEOPT_IF(PyTuple_GET_SIZE(seq) != oparg, UNPACK_SEQUENCE);
        #     STAT_INC(UNPACK_SEQUENCE, hit);
        #     STACK_SHRINK(1);
        #     PyObject **items = _PyTuple_ITEMS(seq);
        #     while (oparg--) {
        #         PUSH(Py_NewRef(items[oparg]));
        #     }
        #     Py_DECREF(seq);
        #     JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE);
        # }
        seq = cls.stack.top()
        cls.flow.deopt_if(not cls.api.PyTuple_CheckExact(seq), 'UNPACK_SEQUENCE')
        cls.flow.deopt_if(cls.api.PyTuple_GET_SIZE(seq) != oparg, 'UNPACK_SEQUENCE')
        cls.flow.stat_inc('UNPACK_SEQUENCE', 'hit')
        cls.stack.shrink(1)
        items = cls.api.private.PyTuple_ITEMS(seq)
        for oparg in range(oparg, 0, -1):
            cls.stack.push(cls.api.Py_NewRef(items[oparg]))
        cls.memory.dec_ref(seq)
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        cls.flow.dispatch()
