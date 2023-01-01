# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCompareOp(OpCode):
    """
    Performs a Boolean operation.  The operation name can be found in
    cmp_op[opname].

    https://docs.python.org/3.12/library/dis.html#opcode-COMPARE_OP
    """
    name = 'COMPARE_OP'
    value = 107

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(COMPARE_OP, (unused/2, left, right -- res)) {
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
        #     ERROR_IF(res == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(oparg <= Py_GE)
        res = cls.api.PyObject_RichCompare(left, right, oparg)
        cls.memory.dec_ref(left)
        cls.memory.dec_ref(right)
        cls.flow.error_if(res == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(2)
        cls.flow.dispatch()
