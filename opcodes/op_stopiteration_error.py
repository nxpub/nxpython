# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStopiterationError(OpCode):
    """
    Handles a StopIteration raised in a generator or coroutine.
    If TOS is an instance of StopIteration, or StopAsyncIteration
    replace it with a RuntimeError.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-STOPITERATION_ERROR
    """
    name = 'STOPITERATION_ERROR'
    value = 63

    @classmethod
    def logic(cls) -> None:
        # inst(STOPITERATION_ERROR) {
        #     assert(frame->owner == FRAME_OWNED_BY_GENERATOR);
        #     PyObject *exc = TOP();
        #     assert(PyExceptionInstance_Check(exc));
        #     const char *msg = NULL;
        #     if (PyErr_GivenExceptionMatches(exc, PyExc_StopIteration)) {
        #         msg = "generator raised StopIteration";
        #         if (frame->f_code->co_flags & CO_ASYNC_GENERATOR) {
        #             msg = "async generator raised StopIteration";
        #         }
        #         else if (frame->f_code->co_flags & CO_COROUTINE) {
        #             msg = "coroutine raised StopIteration";
        #         }
        #     }
        #     else if ((frame->f_code->co_flags & CO_ASYNC_GENERATOR) &&
        #             PyErr_GivenExceptionMatches(exc, PyExc_StopAsyncIteration))
        #     {
        #         /* code in `gen` raised a StopAsyncIteration error:
        #         raise a RuntimeError.
        #         */
        #         msg = "async generator raised StopAsyncIteration";
        #     }
        #     if (msg != NULL) {
        #         PyObject *message = _PyUnicode_FromASCII(msg, strlen(msg));
        #         if (message == NULL) {
        #             goto error;
        #         }
        #         PyObject *error = PyObject_CallOneArg(PyExc_RuntimeError, message);
        #         if (error == NULL) {
        #             Py_DECREF(message);
        #             goto error;
        #         }
        #         assert(PyExceptionInstance_Check(error));
        #         SET_TOP(error);
        #         PyException_SetCause(error, Py_NewRef(exc));
        #         // Steal exc reference, rather than Py_NewRef+Py_DECREF
        #         PyException_SetContext(error, exc);
        #         Py_DECREF(message);
        #     }
        # }
        # assert(frame->owner == FRAME_OWNED_BY_GENERATOR)
        exc = cls.stack.top()
        # assert(PyExceptionInstance_Check(exc))
        const char *msg = None
        if cls.api.PyErr_GivenExceptionMatches(exc, cls.api.PyExc_StopIteration):
            msg = "generator raised StopIteration"
            if frame.f_code.co_flags & CO_ASYNC_GENERATOR:
                msg = "async generator raised StopIteration"
            elif frame.f_code.co_flags & CO_COROUTINE:
                msg = "coroutine raised StopIteration"
        elif frame.f_code.co_flags & CO_ASYNC_GENERATOR:&&
                cls.api.PyErr_GivenExceptionMatches(exc, cls.api.PyExc_StopAsyncIteration))
        {
            # code in `gen` raised a StopAsyncIteration error:
        #     raise a RuntimeError.
        #     
            msg = "async generator raised StopAsyncIteration"
        if msg != None:
            message = cls.api.private.PyUnicode_FromASCII(msg, strlen(msg))
            if message == None:
                cls.flow.error()
            error = cls.api.PyObject_CallOneArg(cls.api.PyExc_RuntimeError, message)
            if error == None:
                cls.memory.dec_ref(message)
                cls.flow.error()
            # assert(PyExceptionInstance_Check(error))
            cls.stack.set_top(error)
            cls.api.PyException_SetCause(error, cls.api.Py_NewRef(exc))
            # Steal exc reference, rather than cls.api.Py_NewRef+Py_DECREF
            cls.api.PyException_SetContext(error, exc)
            cls.memory.dec_ref(message)
        cls.flow.dispatch()
