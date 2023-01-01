# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpEndFor(OpCode):
    """
    Removes the top two values from the stack.
    Equivalent to POP_TOP; POP_TOP.
    Used to clean up at the end of loops, hence the name.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-END_FOR
    """
    name = 'END_FOR'
    value = 4

    @classmethod
    def logic(cls) -> None:
        # macro(END_FOR) = POP_TOP + POP_TOP;
        OpCode['POP_TOP']()
        OpCode['POP_TOP']()
