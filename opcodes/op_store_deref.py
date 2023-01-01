# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreDeref(OpCode):
    """
    Stores TOS into the cell contained in slot i of the “fast locals”
    storage.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_DEREF
    """
    name = 'STORE_DEREF'
    value = 138

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_DEREF, (v --)) {
        #     PyObject *cell = GETLOCAL(oparg);
        #     PyObject *oldobj = PyCell_GET(cell);
        #     PyCell_SET(cell, v);
        #     Py_XDECREF(oldobj);
        # }
        v = cls.stack.peek(1)
        cell = cls.frame.get_local(oparg)
        oldobj = cls.api.PyCell_GET(cell)
        cls.api.PyCell_SET(cell, v)
        cls.memory.dec_ref_x(oldobj)
        cls.stack.shrink(1)
        cls.flow.dispatch()
