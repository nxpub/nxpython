# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwLen(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_LEN'
    value = 41

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_LEN) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     /* len(o) */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     DEOPT_IF(total_args != 1, CALL);
        #     PyObject *callable = PEEK(total_args + 1);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.len, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = TOP();
        #     Py_ssize_t len_i = PyObject_Length(arg);
        #     if (len_i < 0) {
        #         goto error;
        #     }
        #     PyObject *res = PyLong_FromSsize_t(len_i);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     Py_DECREF(callable);
        #     Py_DECREF(arg);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        # }
        # assert(cframe.use_tracing == 0)
        # assert(kwnames == NULL)
        # len(o) 
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        cls.flow.deopt_if(total_args != 1, 'CALL')
        callable = cls.stack.peek(total_args + 1)
        interp = cls.api.private.PyInterpreterState_GET()
        cls.flow.deopt_if(callable != interp.callable_cache.len, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        arg = cls.stack.top()
        len_i = cls.api.PyObject_Length(arg)
        if len_i < 0:
            cls.flow.error()
        res = cls.api.PyLong_FromSsize_t(len_i)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))

        cls.stack.shrink(2-is_meth)
        cls.stack.set_top(res)
        cls.memory.dec_ref(callable)
        cls.memory.dec_ref(arg)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.dispatch()
