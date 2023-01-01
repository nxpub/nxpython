# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwMethodDescriptorNoargs(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS'
    value = 44

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS) {
        #     assert(kwnames == NULL);
        #     assert(oparg == 0 || oparg == 1);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     DEOPT_IF(total_args != 1, CALL);
        #     PyMethodDescrObject *callable = (PyMethodDescrObject *)SECOND();
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     PyObject *self = TOP();
        #     DEOPT_IF(!Py_IS_TYPE(self, callable->d_common.d_type), CALL);
        #     DEOPT_IF(meth->ml_flags != METH_NOARGS, CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = meth->ml_meth;
        #     // This is slower but CPython promises to check all non-vectorcall
        #     // function calls.
        #     if (_Py_EnterRecursiveCallTstate(tstate, " while calling a Python object")) {
        #         goto error;
        #     }
        #     PyObject *res = _PyCFunction_TrampolineCall(cfunc, self, NULL);
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     Py_DECREF(self);
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
        # assert(oparg == 0 || oparg == 1)
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        cls.flow.deopt_if(total_args != 1, 'CALL')
        callable = cls.stack.second()
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(callable, 'PyMethodDescr_Type'), CALL)
        meth = callable.d_method
        self = cls.stack.top()
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(self, 'callable.d_common.d_type'), CALL)
        cls.flow.deopt_if(meth.ml_flags != METH_NOARGS, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        cfunc = meth.ml_meth
        # This is slower but CPython promises to check all non-vectorcall
        # function calls.
        if cls.api.private.Py_EnterRecursiveCallTstate(cls.frame.state, " while calling a cls.api.Python object"):
            cls.flow.error()
        res = cls.api.private.PyCFunction_TrampolineCall(cfunc, self, None)
        cls.api.private.Py_LeaveRecursiveCallTstate(cls.frame.state)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))
        cls.memory.dec_ref(self)
        cls.stack.shrink(oparg + 1)
        cls.stack.set_top(res)
        cls.memory.dec_ref(callable)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
