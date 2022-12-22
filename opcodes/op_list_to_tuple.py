# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpListToTuple(OpCode):
    """
    Pops a list from the stack and pushes a tuple containing the same values.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_TO_TUPLE
    """
    OPCODE_NAME = 'LIST_TO_TUPLE'
    OPCODE_VALUE = 82

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LIST_TO_TUPLE) {
        #     PyObject *list = POP();
        #     PyObject *tuple = PyList_AsTuple(list);
        #     Py_DECREF(list);
        #     if (tuple == NULL) {
        #         goto error;
        #     }
        #     PUSH(tuple);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
