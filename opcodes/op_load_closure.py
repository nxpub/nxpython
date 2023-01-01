# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadClosure(OpCode):
    """
    Pushes a reference to the cell contained in slot i of the “fast locals”
    storage.  The name of the variable is co_fastlocalnames[i].
    
    Note that LOAD_CLOSURE is effectively an alias for LOAD_FAST.
    It exists to keep bytecode a little more readable.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CLOSURE
    """
    name = 'LOAD_CLOSURE'
    value = 136

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_CLOSURE, (-- value)) {
        #     /* We keep LOAD_CLOSURE so that the bytecode stays more readable. */
        #     value = GETLOCAL(oparg);
        #     ERROR_IF(value == NULL, unbound_local_error);
        #     Py_INCREF(value);
        # }
        # We keep LOAD_CLOSURE so that the bytecode stays more readable. 
        value = cls.frame.get_local(oparg)
        cls.flow.unbound_local_error_if(value == None)
        cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
