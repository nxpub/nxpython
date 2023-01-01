# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCleanupThrow(OpCode):
    """
    Handles an exception raised during a throw() or
    close() call through the current frame.  If TOS is an
    instance of StopIteration, pop three values from the stack and push
    its value member.  Otherwise, re-raise TOS.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-CLEANUP_THROW
    """
    name = 'CLEANUP_THROW'
    value = 55

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __1 -- )
        # inst(CLEANUP_THROW) {
        #     assert(throwflag);
        #     PyObject *exc_value = TOP();
        #     assert(exc_value && PyExceptionInstance_Check(exc_value));
        #     if (PyErr_GivenExceptionMatches(exc_value, PyExc_StopIteration)) {
        #         PyObject *value = ((PyStopIterationObject *)exc_value)->value;
        #         Py_INCREF(value);
        #         Py_DECREF(POP());  // The StopIteration.
        #         Py_DECREF(POP());  // The last sent value.
        #         Py_DECREF(POP());  // The delegated sub-iterator.
        #         PUSH(value);
        #     }
        #     else {
        #         PyObject *exc_type = Py_NewRef(Py_TYPE(exc_value));
        #         PyObject *exc_traceback = PyException_GetTraceback(exc_value);
        #         _PyErr_Restore(tstate, exc_type, Py_NewRef(exc_value), exc_traceback);
        #         goto exception_unwind;
        #     }
        # }
        # assert(throwflag)
        exc_value = cls.stack.top()
        # assert(exc_value && PyExceptionInstance_Check(exc_value))
        if cls.api.PyErr_GivenExceptionMatches(exc_value, cls.api.PyExc_StopIteration):
            value = (exc_value).value
            cls.memory.inc_ref(value)
            cls.memory.dec_ref(cls.stack.pop())  # The StopIteration.
            cls.memory.dec_ref(cls.stack.pop())  # The last sent value.
            cls.memory.dec_ref(cls.stack.pop())  # The delegated sub-iterator.
            cls.stack.push(value)
        else:
            exc_type = cls.api.Py_NewRef(cls.api.Py_TYPE(exc_value))
            exc_traceback = cls.api.PyException_GetTraceback(exc_value)
            cls.api.private.PyErr_Restore(cls.frame.state, exc_type, cls.api.Py_NewRef(exc_value), exc_traceback)
            cls.flow.exception_unwind()
        cls.flow.dispatch()
