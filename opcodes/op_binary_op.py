# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOp(OpCode):
    """
    Implements the binary and in-place operators (depending on the value of
    op).
    TOS = TOS1 op TOS.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_OP
    """
    name = 'BINARY_OP'
    value = 122

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(BINARY_OP, (unused/1, lhs, rhs -- res)) {
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
        #     ERROR_IF(res == NULL, error);
        # }
        # static_assert(INLINE_CACHE_ENTRIES_BINARY_OP == 1, "incorrect cache size")
        rhs = cls.stack.peek(1)
        lhs = cls.stack.peek(2)
        # assert(0 <= oparg)
        # assert((unsigned)oparg < Py_ARRAY_LENGTH(binary_ops))
        # assert(binary_ops[oparg])
        res = cls.api.internal.binary_ops[oparg](lhs, rhs)
        cls.memory.dec_ref(lhs)
        cls.memory.dec_ref(rhs)
        cls.flow.error_if(res == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
