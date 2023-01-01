# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwIsinstance(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_ISINSTANCE'
    value = 40

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_ISINSTANCE) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     /* isinstance(o, o2) */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(total_args != 2, CALL);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.isinstance, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *cls = POP();
        #     PyObject *inst = TOP();
        #     int retval = PyObject_IsInstance(inst, cls);
        #     if (retval < 0) {
        #         Py_DECREF(cls);
        #         goto error;
        #     }
        #     PyObject *res = PyBool_FromLong(retval);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     Py_DECREF(inst);
        #     Py_DECREF(cls);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        # }
        # assert(cframe.use_tracing == 0)
        # assert(kwnames == NULL)
        # isinstance(o, o2) 
        is_meth = is_method(cls.stack, oparg)
        total_args = oparg + is_meth
        callable = cls.stack.peek(total_args + 1)
        cls.flow.deopt_if(total_args != 2, 'CALL')
        interp = cls.api.private.PyInterpreterState_GET()
        cls.flow.deopt_if(callable != interp.callable_cache.isinstance, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        cls = cls.stack.pop()
        inst = cls.stack.top()
        retval = cls.api.PyObject_IsInstance(inst, cls)
        if retval < 0:
            cls.memory.dec_ref(cls)
            cls.flow.error()
        res = cls.api.PyBool_FromLong(retval)
        # assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL))

        cls.stack.shrink(2-is_meth)
        cls.stack.set_top(res)
        cls.memory.dec_ref(inst)
        cls.memory.dec_ref(cls)
        cls.memory.dec_ref(callable)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.dispatch()
