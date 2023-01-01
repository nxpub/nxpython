# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadFast(OpCode):
    """
    Pushes a reference to the local co_varnames[var_num] onto the stack.
    
    Changed in version 3.12: This opcode is now only used in situations where the local variable is
    guaranteed to be initialized. It cannot raise UnboundLocalError.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_FAST
    """
    name = 'LOAD_FAST'
    value = 124

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_FAST, (-- value)) {
        #     value = GETLOCAL(oparg);
        #     assert(value != NULL);
        #     Py_INCREF(value);
        # }
        value = cls.frame.get_local(oparg)
        # assert(value != NULL)
        cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
