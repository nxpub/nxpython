# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpInplaceAddUnicode(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_INPLACE_ADD_UNICODE'
    value = 8

    @classmethod
    def logic(cls) -> None:
        # // This is a subtle one. It's a super-instruction for
        # // BINARY_OP_ADD_UNICODE followed by STORE_FAST
        # // where the store goes into the left argument.
        # // So the inputs are the same as for all BINARY_OP
        # // specializations, but there is no output.
        # // At the end we just skip over the STORE_FAST.
        # inst(BINARY_OP_INPLACE_ADD_UNICODE, (left, right --)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyUnicode_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     _Py_CODEUNIT true_next = next_instr[INLINE_CACHE_ENTRIES_BINARY_OP];
        #     assert(_Py_OPCODE(true_next) == STORE_FAST ||
        #            _Py_OPCODE(true_next) == STORE_FAST__LOAD_FAST);
        #     PyObject **target_local = &GETLOCAL(_Py_OPARG(true_next));
        #     DEOPT_IF(*target_local != left, BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     /* Handle `left = left + right` or `left += right` for str.
        #      *
        #      * When possible, extend `left` in place rather than
        #      * allocating a new PyUnicodeObject. This attempts to avoid
        #      * quadratic behavior when one neglects to use str.join().
        #      *
        #      * If `left` has only two references remaining (one from
        #      * the stack, one in the locals), DECREFing `left` leaves
        #      * only the locals reference, so PyUnicode_Append knows
        #      * that the string is safe to mutate.
        #      */
        #     assert(Py_REFCNT(left) >= 2);
        #     _Py_DECREF_NO_DEALLOC(left);
        #     PyUnicode_Append(target_local, right);
        #     _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc);
        #     ERROR_IF(*target_local == NULL, error);
        #     // The STORE_FAST is already done.
        #     JUMPBY(INLINE_CACHE_ENTRIES_BINARY_OP + 1);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyUnicode_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(cls.api.Py_TYPE(right) != cls.api.Py_TYPE(left), 'BINARY_OP')
        true_next = next_instr[INLINE_CACHE_ENTRIES_BINARY_OP]
        # assert(_Py_OPCODE(true_next) == STORE_FAST ||
               cls.api.private.Py_OPCODE(true_next) == STORE_FAST__LOAD_FAST)
        target_local = cls.frame.get_local(cls.api.private.Py_OPARG(true_next))
        cls.flow.deopt_if(*target_local != left, 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        # Handle `left = left + right` or `left += right` for str.
        #  *
        #  * When possible, extend `left` in place rather than
        #  * allocating a new PyUnicodeObject. This attempts to avoid
        #  * quadratic behavior when one neglects to use str.join().
        #  *
        #  * If `left` has only two references remaining (one from
        #  * the stack, one in the locals), DECREFing `left` leaves
        #  * only the locals reference, so PyUnicode_Append knows
        #  * that the string is safe to mutate.
        #  
        # assert(Py_REFCNT(left) >= 2)
        cls.memory.dec_ref_no_dealloc(left)
        cls.api.PyUnicode_Append(target_local, right)
        cls.memory.dec_ref_specialized(right, cls.api.private.PyUnicode_ExactDealloc)
        cls.flow.error_if(*target_local == None, 2)
        # The STORE_FAST is already done.
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_BINARY_OP + 1)
        cls.stack.shrink(2)
        cls.flow.dispatch()
