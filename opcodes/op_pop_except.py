# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPopExcept(OpCode):
    """
    Pops a value from the stack, which is used to restore the exception state.
    
    Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_EXCEPT
    """
    OPCODE_NAME = 'POP_EXCEPT'
    OPCODE_VALUE = 89

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(POP_EXCEPT) {
        #     _PyErr_StackItem *exc_info = tstate->exc_info;
        #     PyObject *value = exc_info->exc_value;
        #     exc_info->exc_value = POP();
        #     Py_XDECREF(value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
