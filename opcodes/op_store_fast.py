# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreFast(OpCode):
    """
    Stores TOS into the local co_varnames[var_num].

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_FAST
    """
    name = 'STORE_FAST'
    value = 125

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_FAST, (value --)) {
        #     SETLOCAL(oparg, value);
        # }
        value = cls.stack.peek(1)
        SETLOCAL(oparg, value)
        cls.stack.shrink(1)
        cls.flow.dispatch()
