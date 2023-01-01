# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadDeref(OpCode):
    """
    Loads the cell contained in slot i of the “fast locals” storage.
    Pushes a reference to the object the cell contains on the stack.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_DEREF
    """
    name = 'LOAD_DEREF'
    value = 137

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_DEREF, ( -- value)) {
        #     PyObject *cell = GETLOCAL(oparg);
        #     value = PyCell_GET(cell);
        #     if (value == NULL) {
        #         format_exc_unbound(tstate, frame->f_code, oparg);
        #         ERROR_IF(true, error);
        #     }
        #     Py_INCREF(value);
        # }
        cell = cls.frame.get_local(oparg)
        value = cls.api.PyCell_GET(cell)
        if value == None:
            format_exc_unbound(cls.frame.state, frame.f_code, oparg)
            cls.flow.error_if(True)
        cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
