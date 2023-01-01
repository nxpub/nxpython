# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteDeref(OpCode):
    """
    Empties the cell contained in slot i of the “fast locals” storage.
    Used by the del statement.
    
    New in version 3.2.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_DEREF
    """
    name = 'DELETE_DEREF'
    value = 139

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DELETE_DEREF, (--)) {
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
        # }
        cell = cls.frame.get_local(oparg)
        oldobj = cls.api.PyCell_GET(cell)
        # Can't use ERROR_IF here.
        # Fortunately we don't need its superpower.
        if oldobj == None:
            format_exc_unbound(cls.frame.state, frame.f_code, oparg)
            cls.flow.error()
        cls.api.PyCell_SET(cell, None)
        cls.memory.dec_ref(oldobj)
        cls.flow.dispatch()
