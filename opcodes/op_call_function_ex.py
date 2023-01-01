# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallFunctionEx(OpCode):
    """
    Calls a callable object with variable set of positional and keyword
    arguments.  If the lowest bit of flags is set, the top of the stack
    contains a mapping object containing additional keyword arguments.
    Before the callable is called, the mapping object and iterable object
    are each “unpacked” and their contents passed in as keyword and
    positional arguments respectively.
    CALL_FUNCTION_EX pops all arguments and the callable object off the stack,
    calls the callable object with those arguments, and pushes the return value
    returned by the callable object.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-CALL_FUNCTION_EX
    """
    name = 'CALL_FUNCTION_EX'
    value = 142

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: CALL_FUNCTION_EX has irregular stack effect
        # inst(CALL_FUNCTION_EX) {
        #     PyObject *func, *callargs, *kwargs = NULL, *result;
        #     if (oparg & 0x01) {
        #         kwargs = POP();
        #         // DICT_MERGE is called before this opcode if there are kwargs.
        #         // It converts all dict subtypes in kwargs into regular dicts.
        #         assert(PyDict_CheckExact(kwargs));
        #     }
        #     callargs = POP();
        #     func = TOP();
        #     if (!PyTuple_CheckExact(callargs)) {
        #         if (check_args_iterable(tstate, func, callargs) < 0) {
        #             Py_DECREF(callargs);
        #             goto error;
        #         }
        #         Py_SETREF(callargs, PySequence_Tuple(callargs));
        #         if (callargs == NULL) {
        #             goto error;
        #         }
        #     }
        #     assert(PyTuple_CheckExact(callargs));

        #     result = do_call_core(tstate, func, callargs, kwargs, cframe.use_tracing);
        #     Py_DECREF(func);
        #     Py_DECREF(callargs);
        #     Py_XDECREF(kwargs);

        #     STACK_SHRINK(1);
        #     assert(TOP() == NULL);
        #     SET_TOP(result);
        #     if (result == NULL) {
        #         goto error;
        #     }
        #     CHECK_EVAL_BREAKER();
        # }
        func, *callargs, *kwargs = None, *result
        if oparg & 0x01:
            kwargs = cls.stack.pop()
            # DICT_MERGE is called before this opcode if there are kwargs.
            # It converts all dict subtypes in kwargs into regular dicts.
            # assert(PyDict_CheckExact(kwargs))
        callargs = cls.stack.pop()
        func = cls.stack.top()
        if not cls.api.PyTuple_CheckExact(callargs):
            if check_args_iterable(cls.frame.state, func, callargs) < 0:
                cls.memory.dec_ref(callargs)
                cls.flow.error()
            cls.api.Py_SETREF(callargs, cls.api.PySequence_Tuple(callargs))
            if callargs == None:
                cls.flow.error()
        # assert(PyTuple_CheckExact(callargs))

        result = do_call_core(cls.frame.state, func, callargs, kwargs, cframe.use_tracing)
        cls.memory.dec_ref(func)
        cls.memory.dec_ref(callargs)
        cls.memory.dec_ref_x(kwargs)

        cls.stack.shrink(1)
        # assert(TOP() == NULL)
        cls.stack.set_top(result)
        if result == None:
            cls.flow.error()
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
