# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpJumpForward(OpCode):
    """
    Increments bytecode counter by delta.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_FORWARD
    """
    name = 'JUMP_FORWARD'
    value = 110

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(JUMP_FORWARD, (--)) {
        #     JUMPBY(oparg);
        # }
        cls.flow.jump_by(oparg)
        cls.flow.dispatch()
