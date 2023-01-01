# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPopTop(OpCode):
    """
    Removes the top-of-stack (TOS) item.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_TOP
    """
    name = 'POP_TOP'
    value = 1

    @classmethod
    def logic(cls) -> None:
        # inst(POP_TOP, (value --)) {
        #     DECREF_INPUTS();
        # }
        value = cls.stack.peek(1)
        cls.memory.dec_ref(value)
        cls.stack.shrink(1)
        cls.flow.dispatch()
