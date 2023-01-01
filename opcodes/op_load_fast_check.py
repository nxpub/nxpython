# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadFastCheck(OpCode):
    """
    Pushes a reference to the local co_varnames[var_num] onto the stack,
    raising an UnboundLocalError if the local variable has not been
    initialized.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_FAST_CHECK
    """
    name = 'LOAD_FAST_CHECK'
    value = 127

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_FAST_CHECK, (-- value)) {
        #     value = GETLOCAL(oparg);
        #     ERROR_IF(value == NULL, unbound_local_error);
        #     Py_INCREF(value);
        # }
        value = cls.frame.get_local(oparg)
        cls.flow.unbound_local_error_if(value == None)
        cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
