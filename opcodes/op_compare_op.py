# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCompareOp(BaseOpCode):
    """
    Performs a Boolean operation.  The operation name can be found in
    cmp_op[opname].

    https://docs.python.org/3.12/library/dis.html#opcode-COMPARE_OP
    """
    OPCODE_NAME = 'COMPARE_OP'
    OPCODE_VALUE = 107

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, left, right) -> None:
        # TARGET(COMPARE_OP) {
        #     PREDICTED(COMPARE_OP);
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
        #     PyObject *res;
        #     _PyCompareOpCache *cache = (_PyCompareOpCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_CompareOp(left, right, next_instr, oparg);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(COMPARE_OP, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     assert(oparg <= Py_GE);
        #     res = PyObject_RichCompare(left, right, oparg);
        #     Py_DECREF(left);
        #     Py_DECREF(right);
        #     if (res == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
