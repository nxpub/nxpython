# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPopExcept(OpCode):
    """
    Pops a value from the stack, which is used to restore the exception state.
    
    Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_EXCEPT
    """
    name = 'POP_EXCEPT'
    value = 89

    @classmethod
    def logic(cls) -> None:
        # inst(POP_EXCEPT, (exc_value -- )) {
        #     _PyErr_StackItem *exc_info = tstate->exc_info;
        #     Py_XSETREF(exc_info->exc_value, exc_value);
        # }
        exc_value = cls.stack.peek(1)
        exc_info = cls.frame.state.exc_info
        cls.api.Py_XSETREF(exc_info.exc_value, exc_value)
        cls.stack.shrink(1)
        cls.flow.dispatch()
