# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpForIterTuple(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'FOR_ITER_TUPLE'
    OPCODE_VALUE = 62

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(FOR_ITER_TUPLE) {
        #     assert(cframe.use_tracing == 0);
        #     _PyTupleIterObject *it = (_PyTupleIterObject *)TOP();
        #     DEOPT_IF(Py_TYPE(it) != &PyTupleIter_Type, FOR_ITER);
        #     STAT_INC(FOR_ITER, hit);
        #     PyTupleObject *seq = it->it_seq;
        #     if (seq) {
        #         if (it->it_index < PyTuple_GET_SIZE(seq)) {
        #             PyObject *next = PyTuple_GET_ITEM(seq, it->it_index++);
        #             PUSH(Py_NewRef(next));
        #             JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER);
        #             goto end_for_iter_tuple;  // End of this instruction
        #         }
        #         it->it_seq = NULL;
        #         Py_DECREF(seq);
        #     }
        #     STACK_SHRINK(1);
        #     Py_DECREF(it);
        #     JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1);
        #     for_iter_tuple:
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
