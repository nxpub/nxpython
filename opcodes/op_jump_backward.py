# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpJumpBackward(OpCode):
    """
    Decrements bytecode counter by delta. Checks for interrupts.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_BACKWARD
    """
    name = 'JUMP_BACKWARD'
    value = 140

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(JUMP_BACKWARD, (--)) {
        #     assert(oparg < INSTR_OFFSET());
        #     JUMPBY(-oparg);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(oparg < INSTR_OFFSET())
        cls.flow.jump_by(-oparg)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
