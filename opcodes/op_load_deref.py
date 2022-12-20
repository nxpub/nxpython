# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadDeref(BaseOpCode):
    """
    Loads the cell contained in slot i of the “fast locals” storage.
    Pushes a reference to the object the cell contains on the stack.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_DEREF
    """
    OPCODE_NAME = 'LOAD_DEREF'
    OPCODE_VALUE = 137

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_DEREF) {
        #     PyObject *cell = GETLOCAL(oparg);
        #     PyObject *value = PyCell_GET(cell);
        #     if (value == NULL) {
        #         format_exc_unbound(tstate, frame->f_code, oparg);
        #         goto error;
        #     }
        #     PUSH(Py_NewRef(value));
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
