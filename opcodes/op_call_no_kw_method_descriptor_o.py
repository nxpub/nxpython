# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwMethodDescriptorO(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_METHOD_DESCRIPTOR_O'
    value = 45

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_METHOD_DESCRIPTOR_O) {
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyMethodDescrObject *callable =
        #         (PyMethodDescrObject *)PEEK(total_args + 1);
        #     DEOPT_IF(total_args != 2, CALL);
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     DEOPT_IF(meth->ml_flags != METH_O, CALL);
        #     PyObject *arg = TOP();
        #     PyObject *self = SECOND();
        #     DEOPT_IF(!Py_IS_TYPE(self, callable->d_common.d_type), CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = meth->ml_meth;
        #     // This is slower but CPython promises to check all non-vectorcall
        #     // function calls.
        #     if (_Py_EnterRecursiveCallTstate(tstate, " while calling a Python object")) {
        #         goto error;
        #     }
        #     PyObject *res = _PyCFunction_TrampolineCall(cfunc, self, arg);
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     Py_DECREF(self);
        #     Py_DECREF(arg);
        #     STACK_SHRINK(oparg + 1);
        #     SET_TOP(res);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(kwnames == NULL)
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        cls.api.PyMethodDescrObject *callable =
            cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(total_args != 2, 'CALL')
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(callable, 'PyMethodDescr_Type'), CALL)
        meth = callable.d_method
        cls.flow.deopt_if(meth.ml_flags != METH_O, 'CALL')
        arg = cls.stack.top()
        self = cls.stack.second()
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(self, 'callable.d_common.d_type'), CALL)
        cls.flow.stat_inc('CALL', 'hit')
        cfunc = meth.ml_meth
        # This is slower but CPython promises to check all non-vectorcall
        # function calls.
        if cls.api.private.Py_EnterRecursiveCallTstate(cls.frame.state, " while calling a cls.api.Python object"):
            cls.flow.error()
        res = cls.api.private.PyCFunction_TrampolineCall(cfunc, self, arg)
        cls.api.private.Py_LeaveRecursiveCallTstate(cls.frame.state)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))
        cls.memory.dec_ref(self)
        cls.memory.dec_ref(arg)
        cls.stack.shrink(oparg + 1)
        cls.stack.set_top(res)
        cls.memory.dec_ref(callable)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
