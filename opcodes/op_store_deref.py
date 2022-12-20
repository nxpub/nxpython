# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreDeref(BaseOpCode):
    """
    Stores TOS into the cell contained in slot i of the “fast locals”
    storage.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_DEREF
    """
    OPCODE_NAME = 'STORE_DEREF'
    OPCODE_VALUE = 138

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(STORE_DEREF) {
        #     PyObject *v = POP();
        #     PyObject *cell = GETLOCAL(oparg);
        #     PyObject *oldobj = PyCell_GET(cell);
        #     PyCell_SET(cell, v);
        #     Py_XDECREF(oldobj);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
