# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMakeCell(BaseOpCode):
    """
    Creates a new cell in slot i.  If that slot is empty then
    that value is stored into the new cell.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-MAKE_CELL
    """
    OPCODE_NAME = 'MAKE_CELL'
    OPCODE_VALUE = 135

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MAKE_CELL) {
        #     // "initial" is probably NULL but not if it's an arg (or set
        #     // via PyFrame_LocalsToFast() before MAKE_CELL has run).
        #     PyObject *initial = GETLOCAL(oparg);
        #     PyObject *cell = PyCell_New(initial);
        #     if (cell == NULL) {
        #         goto resume_with_error;
        #     }
        #     SETLOCAL(oparg, cell);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
