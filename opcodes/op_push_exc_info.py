# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPushExcInfo(OpCode):
    """
    Pops a value from the stack. Pushes the current exception to the top of the stack.
    Pushes the value originally popped back to the stack.
    Used in exception handlers.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-PUSH_EXC_INFO
    """
    name = 'PUSH_EXC_INFO'
    value = 35

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(PUSH_EXC_INFO) {
        #     PyObject *value = TOP();

        #     _PyErr_StackItem *exc_info = tstate->exc_info;
        #     if (exc_info->exc_value != NULL) {
        #         SET_TOP(exc_info->exc_value);
        #     }
        #     else {
        #         SET_TOP(Py_NewRef(Py_None));
        #     }

        #     PUSH(Py_NewRef(value));
        #     assert(PyExceptionInstance_Check(value));
        #     exc_info->exc_value = value;

        # }
        value = cls.stack.top()

        exc_info = cls.frame.state.exc_info
        if exc_info.exc_value != None:
            cls.stack.set_top(exc_info.exc_value)
        else:
            cls.stack.set_top(cls.api.Py_NewRef(cls.api.Py_None))

        cls.stack.push(cls.api.Py_NewRef(value))
        # assert(PyExceptionInstance_Check(value))
        exc_info.exc_value = value
        cls.flow.dispatch()
