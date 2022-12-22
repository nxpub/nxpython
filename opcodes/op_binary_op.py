# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinaryOp(OpCode):
    """
    Implements the binary and in-place operators (depending on the value of
    op).
    TOS = TOS1 op TOS.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_OP
    """
    OPCODE_NAME = 'BINARY_OP'
    OPCODE_VALUE = 122

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, lhs, rhs) -> None:
        # TARGET(BINARY_OP) {
        #     PREDICTED(BINARY_OP);
        #     static_assert(INLINE_CACHE_ENTRIES_BINARY_OP == 1, "incorrect cache size");
        #     PyObject *rhs = PEEK(1);
        #     PyObject *lhs = PEEK(2);
        #     PyObject *res;
        #     _PyBinaryOpCache *cache = (_PyBinaryOpCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_BinaryOp(lhs, rhs, next_instr, oparg, &GETLOCAL(0));
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(BINARY_OP, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     assert(0 <= oparg);
        #     assert((unsigned)oparg < Py_ARRAY_LENGTH(binary_ops));
        #     assert(binary_ops[oparg]);
        #     res = binary_ops[oparg](lhs, rhs);
        #     Py_DECREF(lhs);
        #     Py_DECREF(rhs);
        #     if (res == NULL) goto pop_2_error;
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
