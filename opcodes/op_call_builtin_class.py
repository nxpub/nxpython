# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallBuiltinClass(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_BUILTIN_CLASS'
    value = 28

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_BUILTIN_CLASS) {
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     int kwnames_len = KWNAMES_LEN();
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyType_Check(callable), CALL);
        #     PyTypeObject *tp = (PyTypeObject *)callable;
        #     DEOPT_IF(tp->tp_vectorcall == NULL, CALL);
        #     STAT_INC(CALL, hit);
        #     STACK_SHRINK(total_args);
        #     PyObject *res = tp->tp_vectorcall((PyObject *)tp, stack_pointer,
        #                                       total_args-kwnames_len, kwnames);
        #     kwnames = NULL;
        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     Py_DECREF(tp);
        #     STACK_SHRINK(1-is_meth);
        #     SET_TOP(res);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        kwnames_len = KWNAMES_LEN()
        callable = cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(not cls.api.PyType_Check(callable), 'CALL')
        tp = callable
        cls.flow.deopt_if(tp.tp_vectorcall == None, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        cls.stack.shrink(total_args)
        res = tp.tp_vectorcall(tp, cls.stack,
                                          total_args-kwnames_len, kwnames)
        kwnames = None
        # Free the arguments. 
        for i in range(0, total_args, +1):
            cls.memory.dec_ref(cls.stack[i])
        cls.memory.dec_ref(tp)
        cls.stack.shrink(1-is_meth)
        cls.stack.set_top(res)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
