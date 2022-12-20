# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBinaryOpInplaceAddUnicode(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_OP_INPLACE_ADD_UNICODE'
    OPCODE_VALUE = 8

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, left, right) -> None:
        # TARGET(BINARY_OP_INPLACE_ADD_UNICODE) {
        #     PyObject *right = PEEK(1);
        #     PyObject *left = PEEK(2);
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
        #     if (*target_local == NULL) goto pop_2_error;
        #     // The STORE_FAST is already done.
        #     JUMPBY(INLINE_CACHE_ENTRIES_BINARY_OP + 1);
        #     STACK_SHRINK(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
