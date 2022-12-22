# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpUnpackSequenceList(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'UNPACK_SEQUENCE_LIST'
    OPCODE_VALUE = 168

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(UNPACK_SEQUENCE_LIST) {
        #     PyObject *seq = TOP();
        #     DEOPT_IF(!PyList_CheckExact(seq), UNPACK_SEQUENCE);
        #     DEOPT_IF(PyList_GET_SIZE(seq) != oparg, UNPACK_SEQUENCE);
        #     STAT_INC(UNPACK_SEQUENCE, hit);
        #     STACK_SHRINK(1);
        #     PyObject **items = _PyList_ITEMS(seq);
        #     while (oparg--) {
        #         PUSH(Py_NewRef(items[oparg]));
        #     }
        #     Py_DECREF(seq);
        #     JUMPBY(INLINE_CACHE_ENTRIES_UNPACK_SEQUENCE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
