# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwMethodDescriptorFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_METHOD_DESCRIPTOR_FAST'
    value = 43

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_METHOD_DESCRIPTOR_FAST) {
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyMethodDescrObject *callable =
        #         (PyMethodDescrObject *)PEEK(total_args + 1);
        #     /* Builtin METH_FASTCALL methods, without keywords */
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     DEOPT_IF(meth->ml_flags != METH_FASTCALL, CALL);
        #     PyObject *self = PEEK(total_args);
        #     DEOPT_IF(!Py_IS_TYPE(self, callable->d_common.d_type), CALL);
        #     STAT_INC(CALL, hit);
        #     _PyCFunctionFast cfunc =
        #         (_PyCFunctionFast)(void(*)(void))meth->ml_meth;
        #     int nargs = total_args-1;
        #     STACK_SHRINK(nargs);
        #     PyObject *res = cfunc(self, stack_pointer, nargs);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     /* Clear the stack of the arguments. */
        #     for (int i = 0; i < nargs; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     Py_DECREF(self);
        #     STACK_SHRINK(2-is_meth);
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
        # Builtin METH_FASTCALL methods, without keywords 
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(callable, 'PyMethodDescr_Type'), CALL)
        meth = callable.d_method
        cls.flow.deopt_if(meth.ml_flags != METH_FASTCALL, 'CALL')
        self = cls.stack.peek(total_args)
        cls.flow.deopt_if(not cls.api.Py_IS_TYPE(self, 'callable.d_common.d_type'), CALL)
        cls.flow.stat_inc('CALL', 'hit')
        cls.api.private.PyCFunctionFast cfunc =
            (cls.api.private.PyCFunctionFast)(void(*)(void))meth.ml_meth
        nargs = total_args-1
        cls.stack.shrink(nargs)
        res = cfunc(self, cls.stack, nargs)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))
        # Clear the stack of the arguments. 
        for i in range(0, nargs, +1):
            cls.memory.dec_ref(cls.stack[i])
        cls.memory.dec_ref(self)
        cls.stack.shrink(2-is_meth)
        cls.stack.set_top(res)
        cls.memory.dec_ref(callable)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
