# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCopy(OpCode):
    """
    Push the i-th item to the top of the stack. The item is not removed from its
    original location.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-COPY
    """
    OPCODE_NAME = 'COPY'
    OPCODE_VALUE = 120

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(COPY) {
        #     assert(oparg != 0);
        #     PyObject *peek = PEEK(oparg);
        #     PUSH(Py_NewRef(peek));
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
