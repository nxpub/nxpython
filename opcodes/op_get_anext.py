# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpGetAnext(OpCode):
    """
    Pushes get_awaitable(TOS.__anext__()) to the stack.  See
    GET_AWAITABLE for details about get_awaitable.
    
    New in version 3.5.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_ANEXT
    """
    name = 'GET_ANEXT'
    value = 51

    @classmethod
    def logic(cls) -> None:
        # inst(GET_ANEXT, (aiter -- aiter, awaitable)) {
        #     unaryfunc getter = NULL;
        #     PyObject *next_iter = NULL;
        #     PyTypeObject *type = Py_TYPE(aiter);

        #     if (PyAsyncGen_CheckExact(aiter)) {
        #         awaitable = type->tp_as_async->am_anext(aiter);
        #         if (awaitable == NULL) {
        #             goto error;
        #         }
        #     } else {
        #         if (type->tp_as_async != NULL){
        #             getter = type->tp_as_async->am_anext;
        #         }

        #         if (getter != NULL) {
        #             next_iter = (*getter)(aiter);
        #             if (next_iter == NULL) {
        #                 goto error;
        #             }
        #         }
        #         else {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'async for' requires an iterator with "
        #                           "__anext__ method, got %.100s",
        #                           type->tp_name);
        #             goto error;
        #         }

        #         awaitable = _PyCoro_GetAwaitableIter(next_iter);
        #         if (awaitable == NULL) {
        #             _PyErr_FormatFromCause(
        #                 PyExc_TypeError,
        #                 "'async for' received an invalid object "
        #                 "from __anext__: %.100s",
        #                 Py_TYPE(next_iter)->tp_name);

        #             Py_DECREF(next_iter);
        #             goto error;
        #         } else {
        #             Py_DECREF(next_iter);
        #         }
        #     }

        #     PREDICT(LOAD_CONST);
        # }
        aiter = cls.stack.peek(1)
        getter = None
        next_iter = None
        type = cls.api.Py_TYPE(aiter)

        if cls.api.PyAsyncGen_CheckExact(aiter):
            awaitable = type.tp_as_async.am_anext(aiter)
            if awaitable == None:
                cls.flow.error()
        else:
            if type.tp_as_async != None:
                getter = type.tp_as_async.am_anext

            if getter != None:
                next_iter = (*getter)(aiter)
                if next_iter == None:
                    cls.flow.error()
            else:
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                              "'async for' requires an iterator with "
                              "__anext__ method, got %.100s",
                              type.tp_name)
                cls.flow.error()

            awaitable = cls.api.private.PyCoro_GetAwaitableIter(next_iter)
            if awaitable == None:
                cls.api.private.PyErr_FormatFromCause(
                    cls.api.PyExc_TypeError,
                    "'async for' received an invalid object "
                    "from __anext__: %.100s",
                    cls.api.Py_TYPE(next_iter).tp_name)

                cls.memory.dec_ref(next_iter)
                cls.flow.error()
            else:
                cls.memory.dec_ref(next_iter)

        cls.stack.grow(1)
        cls.stack.poke(1, awaitable)
        cls.flow.dispatch()
