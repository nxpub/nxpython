# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwBuiltinFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_BUILTIN_FAST'
    value = 38

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_BUILTIN_FAST) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_FASTCALL functions, without keywords */
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_FASTCALL,
        #         CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = PyCFunction_GET_FUNCTION(callable);
        #     STACK_SHRINK(total_args);
        #     /* res = func(self, args, nargs) */
        #     PyObject *res = ((_PyCFunctionFast)(void(*)(void))cfunc)(
        #         PyCFunction_GET_SELF(callable),
        #         stack_pointer,
        #         total_args);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     PUSH(res);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         /* Not deopting because this doesn't mean our optimization was
        #            wrong. `res` can be NULL for valid reasons. Eg. getattr(x,
        #            'invalid'). In those cases an exception is set, so we must
        #            handle it.
        #         */
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(cframe.use_tracing == 0)
        # Builtin METH_FASTCALL functions, without keywords 
        # assert(kwnames == NULL)
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        callable = cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(not cls.api.PyCFunction_CheckExact(callable), 'CALL')
        DEOPT_IF(cls.api.PyCFunction_GET_FLAGS(callable) != METH_FASTCALL,
            CALL)
        cls.flow.stat_inc('CALL', 'hit')
        cfunc = cls.api.PyCFunction_GET_FUNCTION(callable)
        cls.stack.shrink(total_args)
        # res = func(self, args, nargs) 
        res = ((cls.api.private.PyCFunctionFast)(void(*)(void))cfunc)(
            cls.api.PyCFunction_GET_SELF(callable),
            cls.stack,
            total_args)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))

        # Free the arguments. 
        for i in range(0, total_args, +1):
            cls.memory.dec_ref(cls.stack[i])
        cls.stack.shrink(2-is_meth)
        cls.stack.push(res)
        cls.memory.dec_ref(callable)
        if res == None:
            # Not deopting because this doesn't mean our optimization was
        #        wrong. `res` can be NULL for valid reasons. Eg. getattr(x,
        #        'invalid'). In those cases an exception is set, so we must
        #        handle it.
        #     
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
