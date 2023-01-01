# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpNop(OpCode):
    """
    Do nothing code.  Used as a placeholder by the bytecode optimizer, and to
    generate line tracing events.

    https://docs.python.org/3.12/library/dis.html#opcode-NOP
    """
    name = 'NOP'
    value = 9

    @classmethod
    def logic(cls) -> None:
        # inst(NOP, (--)) {
        # }
        cls.flow.dispatch()
