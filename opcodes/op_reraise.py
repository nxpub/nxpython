# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpReraise(OpCode):
    """
    Re-raises the exception currently on top of the stack. If oparg is non-zero,
    pops an additional value from the stack which is used to set f_lasti
    of the current frame.
    
    New in version 3.9.
    
    Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-RERAISE
    """
    name = 'RERAISE'
    value = 119

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- )
        # inst(RERAISE) {
        #     if (oparg) {
        #         PyObject *lasti = PEEK(oparg + 1);
        #         if (PyLong_Check(lasti)) {
        #             frame->prev_instr = _PyCode_CODE(frame->f_code) + PyLong_AsLong(lasti);
        #             assert(!_PyErr_Occurred(tstate));
        #         }
        #         else {
        #             assert(PyLong_Check(lasti));
        #             _PyErr_SetString(tstate, PyExc_SystemError, "lasti is not an int");
        #             goto error;
        #         }
        #     }
        #     PyObject *val = POP();
        #     assert(val && PyExceptionInstance_Check(val));
        #     PyObject *exc = Py_NewRef(PyExceptionInstance_Class(val));
        #     PyObject *tb = PyException_GetTraceback(val);
        #     _PyErr_Restore(tstate, exc, val, tb);
        #     goto exception_unwind;
        # }
        if oparg:
            lasti = cls.stack.peek(oparg + 1)
            if cls.api.PyLong_Check(lasti):
                frame.prev_instr = cls.api.private.PyCode_CODE(frame.f_code) + cls.api.PyLong_AsLong(lasti)
                # assert(!_PyErr_Occurred(tstate))
            else:
                # assert(PyLong_Check(lasti))
                cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_SystemError, "lasti is not an int")
                cls.flow.error()
        val = cls.stack.pop()
        # assert(val && PyExceptionInstance_Check(val))
        exc = cls.api.Py_NewRef(cls.api.PyExceptionInstance_Class(val))
        tb = cls.api.PyException_GetTraceback(val)
        cls.api.private.PyErr_Restore(cls.frame.state, exc, val, tb)
        cls.flow.exception_unwind()
