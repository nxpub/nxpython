# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpDeleteDeref(OpCode):
    """
    Empties the cell contained in slot i of the “fast locals” storage.
    Used by the del statement.
    
    New in version 3.2.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_DEREF
    """
    OPCODE_NAME = 'DELETE_DEREF'
    OPCODE_VALUE = 139

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DELETE_DEREF) {
        #     PyObject *cell = GETLOCAL(oparg);
        #     PyObject *oldobj = PyCell_GET(cell);
        #     // Can't use ERROR_IF here.
        #     // Fortunately we don't need its superpower.
        #     if (oldobj == NULL) {
        #         format_exc_unbound(tstate, frame->f_code, oparg);
        #         goto error;
        #     }
        #     PyCell_SET(cell, NULL);
        #     Py_DECREF(oldobj);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
