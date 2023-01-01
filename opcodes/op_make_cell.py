# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpMakeCell(OpCode):
    """
    Creates a new cell in slot i.  If that slot is empty then
    that value is stored into the new cell.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-MAKE_CELL
    """
    name = 'MAKE_CELL'
    value = 135

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(MAKE_CELL, (--)) {
        #     // "initial" is probably NULL but not if it's an arg (or set
        #     // via PyFrame_LocalsToFast() before MAKE_CELL has run).
        #     PyObject *initial = GETLOCAL(oparg);
        #     PyObject *cell = PyCell_New(initial);
        #     if (cell == NULL) {
        #         goto resume_with_error;
        #     }
        #     SETLOCAL(oparg, cell);
        # }
        # "initial" is probably None but not if it's an arg (or set
        # via cls.api.PyFrame_LocalsToFast() before MAKE_CELL has run).
        initial = cls.frame.get_local(oparg)
        cell = cls.api.PyCell_New(initial)
        if cell == None:
            cls.flow.resume_with_error()
        SETLOCAL(oparg, cell)
        cls.flow.dispatch()
