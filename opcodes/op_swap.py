# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpSwap(BaseOpCode):
    """
    Swap TOS with the item at position i.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-SWAP
    """
    OPCODE_NAME = 'SWAP'
    OPCODE_VALUE = 99

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(SWAP) {
        #     assert(oparg != 0);
        #     PyObject *top = TOP();
        #     SET_TOP(PEEK(oparg));
        #     PEEK(oparg) = top;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
