# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpUnpackSequenceTwoTuple(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'UNPACK_SEQUENCE_TWO_TUPLE'
    OPCODE_VALUE = 170

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(UNPACK_SEQUENCE_TWO_TUPLE) {
        #     PyObject *seq = TOP();
        #     DEOPT_IF(!PyTuple_CheckExact(seq), UNPACK_SEQUENCE);
        #     DEOPT_IF(PyTuple_GET_SIZE(seq) != 2, UNPACK_SEQUENCE);
        #     STAT_INC(UNPACK_SEQUENCE, hit);
        #     SET_TOP(Py_NewRef(PyTuple_GET_ITEM(seq, 1)));
        #     PUSH(Py_NewRef(PyTuple_GET_ITEM(seq, 0)));
        #     Py_DECREF(seq);
        #     JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
