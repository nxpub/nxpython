# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpForIterRange(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'FOR_ITER_RANGE'
    OPCODE_VALUE = 64

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(FOR_ITER_RANGE) {
        #     assert(cframe.use_tracing == 0);
        #     _PyRangeIterObject *r = (_PyRangeIterObject *)TOP();
        #     DEOPT_IF(Py_TYPE(r) != &PyRangeIter_Type, FOR_ITER);
        #     STAT_INC(FOR_ITER, hit);
        #     _Py_CODEUNIT next = next_instr[INLINE_CACHE_ENTRIES_FOR_ITER];
        #     assert(_PyOpcode_Deopt[_Py_OPCODE(next)] == STORE_FAST);
        #     if (r->len <= 0) {
        #         STACK_SHRINK(1);
        #         Py_DECREF(r);
        #         JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1);
        #     }
        #     else {
        #         long value = r->start;
        #         r->start = value + r->step;
        #         r->len--;
        #         if (_PyLong_AssignValue(&GETLOCAL(_Py_OPARG(next)), value) < 0) {
        #             goto error;
        #         }
        #         // The STORE_FAST is already done.
        #         JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + 1);
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
