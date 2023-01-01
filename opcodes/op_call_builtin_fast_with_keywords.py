# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallBuiltinFastWithKeywords(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_BUILTIN_FAST_WITH_KEYWORDS'
    value = 29

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_BUILTIN_FAST_WITH_KEYWORDS) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_FASTCALL | METH_KEYWORDS functions */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) !=
        #         (METH_FASTCALL | METH_KEYWORDS), CALL);
        #     STAT_INC(CALL, hit);
        #     STACK_SHRINK(total_args);
        #     /* res = func(self, args, nargs, kwnames) */
        #     _PyCFunctionFastWithKeywords cfunc =
        #         (_PyCFunctionFastWithKeywords)(void(*)(void))
        #         PyCFunction_GET_FUNCTION(callable);
        #     PyObject *res = cfunc(
        #         PyCFunction_GET_SELF(callable),
        #         stack_pointer,
        #         total_args - KWNAMES_LEN(),
        #         kwnames
        #     );
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     kwnames = NULL;

        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     PUSH(res);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(cframe.use_tracing == 0)
        # Builtin METH_FASTCALL | METH_KEYWORDS functions 
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        callable = cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(not cls.api.PyCFunction_CheckExact(callable), 'CALL')
        DEOPT_IF(cls.api.PyCFunction_GET_FLAGS(callable) !=
            (METH_FASTCALL | METH_KEYWORDS), CALL)
        cls.flow.stat_inc('CALL', 'hit')
        cls.stack.shrink(total_args)
        # res = func(self, args, nargs, kwnames) 
        cls.api.private.PyCFunctionFastWithKeywords cfunc =
            (cls.api.private.PyCFunctionFastWithKeywords)(void(*)(void))
            cls.api.PyCFunction_GET_FUNCTION(callable)
        res = cfunc(
            cls.api.PyCFunction_GET_SELF(callable),
            cls.stack,
            total_args - KWNAMES_LEN(),
            kwnames
        )
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))
        kwnames = None

        # Free the arguments. 
        for i in range(0, total_args, +1):
            cls.memory.dec_ref(cls.stack[i])
        cls.stack.shrink(2-is_meth)
        cls.stack.push(res)
        cls.memory.dec_ref(callable)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
