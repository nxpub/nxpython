# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpForIterRange(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'FOR_ITER_RANGE'
    value = 64

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(FOR_ITER_RANGE) {
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
        # }
        # assert(cframe.use_tracing == 0)
        r = cls.stack.top()
        cls.flow.deopt_if(cls.api.Py_TYPE(r) != cls.api.PyRangeIter_Type, 'FOR_ITER')
        cls.flow.stat_inc('FOR_ITER', 'hit')
        next = next_instr[INLINE_CACHE_ENTRIES_FOR_ITER]
        # assert(_PyOpcode_Deopt[_Py_OPCODE(next)] == STORE_FAST)
        if r.len <= 0:
            cls.stack.shrink(1)
            cls.memory.dec_ref(r)
            cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1)
        else:
            value = r.start
            r.start = value + r.step
            r.len--
            if cls.api.private.PyLong_AssignValue(cls.frame.get_local(cls.api.private.Py_OPARG(next)), value) < 0:
                cls.flow.error()
            # The STORE_FAST is already done.
            cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER + 1)
        cls.flow.dispatch()
