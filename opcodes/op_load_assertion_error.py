# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpLoadAssertionError(OpCode):
    """
    Pushes AssertionError onto the stack.  Used by the assert
    statement.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_ASSERTION_ERROR
    """
    OPCODE_NAME = 'LOAD_ASSERTION_ERROR'
    OPCODE_VALUE = 74

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_ASSERTION_ERROR) {
        #     PyObject *value = PyExc_AssertionError;
        #     PUSH(Py_NewRef(value));
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
