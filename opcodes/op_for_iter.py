# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpForIter(OpCode):
    """
    TOS is an iterator.  Call its __next__() method.  If
    this yields a new value, push it on the stack (leaving the iterator below
    it).  If the iterator indicates it is exhausted then the byte
    code counter is incremented by delta.
    
    Changed in version 3.12: Up until 3.11 the iterator was popped when it was exhausted.

    https://docs.python.org/3.12/library/dis.html#opcode-FOR_ITER
    """
    name = 'FOR_ITER'
    value = 93

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: ( -- __0)
        # inst(FOR_ITER) {
        #     _PyForIterCache *cache = (_PyForIterCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         next_instr--;
        #         _Py_Specialize_ForIter(TOP(), next_instr, oparg);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(FOR_ITER, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     /* before: [iter]; after: [iter, iter()] *or* [] */
        #     PyObject *iter = TOP();
        #     PyObject *next = (*Py_TYPE(iter)->tp_iternext)(iter);
        #     if (next != NULL) {
        #         PUSH(next);
        #         JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER);
        #     }
        #     else {
        #         if (_PyErr_Occurred(tstate)) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_StopIteration)) {
        #                 goto error;
        #             }
        #             else if (tstate->c_tracefunc != NULL) {
        #                 call_exc_trace(tstate->c_tracefunc, tstate->c_traceobj, tstate, frame);
        #             }
        #             _PyErr_Clear(tstate);
        #         }
        #         /* iterator ended normally */
        #         assert(_Py_OPCODE(next_instr[INLINE_CACHE_ENTRIES_FOR_ITER + oparg]) == END_FOR);
        #         STACK_SHRINK(1);
        #         Py_DECREF(iter);
        #         /* Skip END_FOR */
        #         JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1);
        #     }
        # }
        # before: [iter] after: [iter, iter()] *or* [] 
        iter = cls.stack.top()
        next = (*Py_TYPE(iter).tp_iternext)(iter)
        if next != None:
            cls.stack.push(next)
            cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER)
        else:
            if cls.api.private.PyErr_Occurred(cls.frame.state):
                if not cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_StopIteration):
                    cls.flow.error()
                elif cls.frame.state.c_tracefunc != None:
                    call_exc_trace(cls.frame.state.c_tracefunc, cls.frame.state.c_traceobj, cls.frame.state, frame)
                cls.api.private.PyErr_Clear(cls.frame.state)
            # iterator ended normally 
            # assert(_Py_OPCODE(next_instr[INLINE_CACHE_ENTRIES_FOR_ITER + oparg]) == END_FOR)
            cls.stack.shrink(1)
            cls.memory.dec_ref(iter)
            # Skip END_FOR 
            cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1)
        cls.flow.dispatch()
