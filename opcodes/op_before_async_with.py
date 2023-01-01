# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBeforeAsyncWith(OpCode):
    """
    Resolves __aenter__ and __aexit__ from the object on top of the
    stack.  Pushes __aexit__ and result of __aenter__() to the stack.
    
    New in version 3.5.

    https://docs.python.org/3.12/library/dis.html#opcode-BEFORE_ASYNC_WITH
    """
    name = 'BEFORE_ASYNC_WITH'
    value = 52

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(BEFORE_ASYNC_WITH) {
        #     PyObject *mgr = TOP();
        #     PyObject *res;
        #     PyObject *enter = _PyObject_LookupSpecial(mgr, &_Py_ID(__aenter__));
        #     if (enter == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "asynchronous context manager protocol",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         goto error;
        #     }
        #     PyObject *exit = _PyObject_LookupSpecial(mgr, &_Py_ID(__aexit__));
        #     if (exit == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "asynchronous context manager protocol "
        #                           "(missed __aexit__ method)",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         Py_DECREF(enter);
        #         goto error;
        #     }
        #     SET_TOP(exit);
        #     Py_DECREF(mgr);
        #     res = _PyObject_CallNoArgs(enter);
        #     Py_DECREF(enter);
        #     if (res == NULL)
        #         goto error;
        #     PUSH(res);
        #     PREDICT(GET_AWAITABLE);
        # }
        mgr = cls.stack.top()
        enter = cls.api.private.PyObject_LookupSpecial(mgr, cls.api.private.Py_ID('__aenter__'))
        if enter == None:
            if not cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                              "'%.200s' object does not support the "
                              "asynchronous context manager protocol",
                              cls.api.Py_TYPE(mgr).tp_name)
            cls.flow.error()
        exit = cls.api.private.PyObject_LookupSpecial(mgr, cls.api.private.Py_ID('__aexit__'))
        if exit == None:
            if not cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                              "'%.200s' object does not support the "
                              "asynchronous context manager protocol "
                              "(missed __aexit__ method)",
                              cls.api.Py_TYPE(mgr).tp_name)
            cls.memory.dec_ref(enter)
            cls.flow.error()
        cls.stack.set_top(exit)
        cls.memory.dec_ref(mgr)
        res = cls.api.private.PyObject_CallNoArgs(enter)
        cls.memory.dec_ref(enter)
        if res == None:
            cls.flow.error()
        cls.stack.push(res)
        cls.flow.dispatch()
