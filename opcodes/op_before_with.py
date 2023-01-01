# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBeforeWith(OpCode):
    """
    This opcode performs several operations before a with block starts.  First,
    it loads __exit__() from the context manager and pushes it onto
    the stack for later use by WITH_EXCEPT_START.  Then,
    __enter__() is called. Finally, the result of calling the
    __enter__() method is pushed onto the stack.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-BEFORE_WITH
    """
    name = 'BEFORE_WITH'
    value = 53

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(BEFORE_WITH) {
        #     PyObject *mgr = TOP();
        #     PyObject *res;
        #     PyObject *enter = _PyObject_LookupSpecial(mgr, &_Py_ID(__enter__));
        #     if (enter == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "context manager protocol",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         goto error;
        #     }
        #     PyObject *exit = _PyObject_LookupSpecial(mgr, &_Py_ID(__exit__));
        #     if (exit == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "context manager protocol "
        #                           "(missed __exit__ method)",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         Py_DECREF(enter);
        #         goto error;
        #     }
        #     SET_TOP(exit);
        #     Py_DECREF(mgr);
        #     res = _PyObject_CallNoArgs(enter);
        #     Py_DECREF(enter);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     PUSH(res);
        # }
        mgr = cls.stack.top()
        enter = cls.api.private.PyObject_LookupSpecial(mgr, cls.api.private.Py_ID('__enter__'))
        if enter == None:
            if not cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                              "'%.200s' object does not support the "
                              "context manager protocol",
                              cls.api.Py_TYPE(mgr).tp_name)
            cls.flow.error()
        exit = cls.api.private.PyObject_LookupSpecial(mgr, cls.api.private.Py_ID('__exit__'))
        if exit == None:
            if not cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                              "'%.200s' object does not support the "
                              "context manager protocol "
                              "(missed __exit__ method)",
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
