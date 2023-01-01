# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPopJumpIfNotNone(OpCode):
    """
    If TOS is not None, increments the bytecode counter by delta.  TOS is popped.
    
    New in version 3.11.
    
    Changed in version 3.12: This is no longer a pseudo-instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_JUMP_IF_NOT_NONE
    """
    name = 'POP_JUMP_IF_NOT_NONE'
    value = 128

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- )
        # inst(POP_JUMP_IF_NOT_NONE) {
        #     PyObject *value = POP();
        #     if (!Py_IsNone(value)) {
        #         JUMPBY(oparg);
        #     }
        #     Py_DECREF(value);
        # }
        value = cls.stack.pop()
        if not cls.api.Py_IsNone(value):
            cls.flow.jump_by(oparg)
        cls.memory.dec_ref(value)
        cls.flow.dispatch()
