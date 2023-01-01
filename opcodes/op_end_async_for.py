# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpEndAsyncFor(OpCode):
    """
    Terminates an async for loop.  Handles an exception raised
    when awaiting a next item.  If TOS is StopAsyncIteration pop 3
    values from the stack and restore the exception state using the second
    of them.  Otherwise re-raise the exception using the value
    from the stack.  An exception handler block is removed from the block stack.
    
    New in version 3.8: 
    
    Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-END_ASYNC_FOR
    """
    name = 'END_ASYNC_FOR'
    value = 54

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __1 -- )
        # inst(END_ASYNC_FOR) {
        #     PyObject *val = POP();
        #     assert(val && PyExceptionInstance_Check(val));
        #     if (PyErr_GivenExceptionMatches(val, PyExc_StopAsyncIteration)) {
        #         Py_DECREF(val);
        #         Py_DECREF(POP());
        #     }
        #     else {
        #         PyObject *exc = Py_NewRef(PyExceptionInstance_Class(val));
        #         PyObject *tb = PyException_GetTraceback(val);
        #         _PyErr_Restore(tstate, exc, val, tb);
        #         goto exception_unwind;
        #     }
        # }
        val = cls.stack.pop()
        # assert(val && PyExceptionInstance_Check(val))
        if cls.api.PyErr_GivenExceptionMatches(val, cls.api.PyExc_StopAsyncIteration):
            cls.memory.dec_ref(val)
            cls.memory.dec_ref(cls.stack.pop())
        else:
            exc = cls.api.Py_NewRef(cls.api.PyExceptionInstance_Class(val))
            tb = cls.api.PyException_GetTraceback(val)
            cls.api.private.PyErr_Restore(cls.frame.state, exc, val, tb)
            cls.flow.exception_unwind()
        cls.flow.dispatch()
