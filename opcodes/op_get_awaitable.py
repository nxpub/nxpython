# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpGetAwaitable(OpCode):
    """
    Implements TOS = get_awaitable(TOS), where get_awaitable(o)
    returns o if o is a coroutine object or a generator object with
    the CO_ITERABLE_COROUTINE flag, or resolves
    o.__await__.
    
    If the where operand is nonzero, it indicates where the instruction
    occurs:
    
    1 After a call to __aenter__
    
    2 After a call to __aexit__
    
    New in version 3.5.
    
    Changed in version 3.11: Previously, this instruction did not have an oparg.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_AWAITABLE
    """
    name = 'GET_AWAITABLE'
    value = 131

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(GET_AWAITABLE, (iterable -- iter)) {
        #     iter = _PyCoro_GetAwaitableIter(iterable);

        #     if (iter == NULL) {
        #         format_awaitable_error(tstate, Py_TYPE(iterable), oparg);
        #     }

        #     DECREF_INPUTS();

        #     if (iter != NULL && PyCoro_CheckExact(iter)) {
        #         PyObject *yf = _PyGen_yf((PyGenObject*)iter);
        #         if (yf != NULL) {
        #             /* `iter` is a coroutine object that is being
        #                awaited, `yf` is a pointer to the current awaitable
        #                being awaited on. */
        #             Py_DECREF(yf);
        #             Py_CLEAR(iter);
        #             _PyErr_SetString(tstate, PyExc_RuntimeError,
        #                              "coroutine is being awaited already");
        #             /* The code below jumps to `error` if `iter` is NULL. */
        #         }
        #     }

        #     ERROR_IF(iter == NULL, error);

        #     PREDICT(LOAD_CONST);
        # }
        iterable = cls.stack.peek(1)
        iter = cls.api.private.PyCoro_GetAwaitableIter(iterable)

        if iter == None:
            format_awaitable_error(cls.frame.state, cls.api.Py_TYPE(iterable), oparg)

        cls.memory.dec_ref(iterable)

        if iter != None and cls.api.PyCoro_CheckExact(iter):
            yf = cls.api.private.PyGen_yf(iter)
            if yf != None:
                # `iter` is a coroutine object that is being
        #            awaited, `yf` is a pointer to the current awaitable
        #            being awaited on. 
                cls.memory.dec_ref(yf)
                cls.api.Py_CLEAR(iter)
                cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_RuntimeError,
                                 "coroutine is being awaited already")
                # The code below jumps to `error` if `iter` is NULL. 

        cls.flow.error_if(iter == None, 1)

        cls.stack.poke(1, iter)
        cls.flow.dispatch()
