# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwBuiltinO(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_BUILTIN_O'
    value = 39

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_BUILTIN_O) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_O functions */
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     DEOPT_IF(total_args != 1, CALL);
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_O, CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = PyCFunction_GET_FUNCTION(callable);
        #     // This is slower but CPython promises to check all non-vectorcall
        #     // function calls.
        #     if (_Py_EnterRecursiveCallTstate(tstate, " while calling a Python object")) {
        #         goto error;
        #     }
        #     PyObject *arg = TOP();
        #     PyObject *res = _PyCFunction_TrampolineCall(cfunc, PyCFunction_GET_SELF(callable), arg);
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     Py_DECREF(arg);
        #     Py_DECREF(callable);
        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(cframe.use_tracing == 0)
        # Builtin METH_O functions 
        # assert(kwnames == NULL)
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        cls.flow.deopt_if(total_args != 1, 'CALL')
        callable = cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(not cls.api.PyCFunction_CheckExact(callable), 'CALL')
        cls.flow.deopt_if(cls.api.PyCFunction_GET_FLAGS(callable) != METH_O, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        cfunc = cls.api.PyCFunction_GET_FUNCTION(callable)
        # This is slower but CPython promises to check all non-vectorcall
        # function calls.
        if cls.api.private.Py_EnterRecursiveCallTstate(cls.frame.state, " while calling a cls.api.Python object"):
            cls.flow.error()
        arg = cls.stack.top()
        res = cls.api.private.PyCFunction_TrampolineCall(cfunc, cls.api.PyCFunction_GET_SELF(callable), arg)
        cls.api.private.Py_LeaveRecursiveCallTstate(cls.frame.state)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))

        cls.memory.dec_ref(arg)
        cls.memory.dec_ref(callable)
        cls.stack.shrink(2-is_meth)
        cls.stack.set_top(res)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
