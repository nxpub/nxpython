# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnpackSequenceTwoTuple(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'UNPACK_SEQUENCE_TWO_TUPLE'
    value = 170

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- __array[oparg])
        # inst(UNPACK_SEQUENCE_TWO_TUPLE) {
        #     PyObject *seq = TOP();
        #     DEOPT_IF(!PyTuple_CheckExact(seq), UNPACK_SEQUENCE);
        #     DEOPT_IF(PyTuple_GET_SIZE(seq) != 2, UNPACK_SEQUENCE);
        #     STAT_INC(UNPACK_SEQUENCE, hit);
        #     SET_TOP(Py_NewRef(PyTuple_GET_ITEM(seq, 1)));
        #     PUSH(Py_NewRef(PyTuple_GET_ITEM(seq, 0)));
        #     Py_DECREF(seq);
        #     JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE);
        # }
        seq = cls.stack.top()
        cls.flow.deopt_if(not cls.api.PyTuple_CheckExact(seq), 'UNPACK_SEQUENCE')
        cls.flow.deopt_if(cls.api.PyTuple_GET_SIZE(seq) != 2, 'UNPACK_SEQUENCE')
        cls.flow.stat_inc('UNPACK_SEQUENCE', 'hit')
        cls.stack.set_top(cls.api.Py_NewRef(cls.api.PyTuple_GET_ITEM(seq, 1)))
        cls.stack.push(cls.api.Py_NewRef(cls.api.PyTuple_GET_ITEM(seq, 0)))
        cls.memory.dec_ref(seq)
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE)
        cls.flow.dispatch()
