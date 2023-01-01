# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadConst(OpCode):
    """
    Pushes co_consts[consti] onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CONST
    """
    name = 'LOAD_CONST'
    value = 100

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_CONST, (-- value)) {
        #     value = GETITEM(consts, oparg);
        #     Py_INCREF(value);
        # }
        value = cls.frame.get_const(oparg)
        cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
