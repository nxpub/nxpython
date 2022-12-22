# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpForIterList(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'FOR_ITER_LIST'
    OPCODE_VALUE = 59

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(FOR_ITER_LIST) {
        #     assert(cframe.use_tracing == 0);
        #     _PyListIterObject *it = (_PyListIterObject *)TOP();
        #     DEOPT_IF(Py_TYPE(it) != &PyListIter_Type, FOR_ITER);
        #     STAT_INC(FOR_ITER, hit);
        #     PyListObject *seq = it->it_seq;
        #     if (seq) {
        #         if (it->it_index < PyList_GET_SIZE(seq)) {
        #             PyObject *next = PyList_GET_ITEM(seq, it->it_index++);
        #             PUSH(Py_NewRef(next));
        #             JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER);
        #             goto end_for_iter_list;  // End of this instruction
        #         }
        #         it->it_seq = NULL;
        #         Py_DECREF(seq);
        #     }
        #     STACK_SHRINK(1);
        #     Py_DECREF(it);
        #     JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1);
        #     for_iter_list:
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
