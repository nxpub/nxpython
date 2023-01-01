# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPopJumpIfNone(OpCode):
    """
    If TOS is None, increments the bytecode counter by delta.  TOS is popped.
    
    New in version 3.11.
    
    Changed in version 3.12: This is no longer a pseudo-instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_JUMP_IF_NONE
    """
    name = 'POP_JUMP_IF_NONE'
    value = 129

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- )
        # inst(POP_JUMP_IF_NONE) {
        #     PyObject *value = POP();
        #     if (Py_IsNone(value)) {
        #         _Py_DECREF_NO_DEALLOC(value);
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         Py_DECREF(value);
        #     }
        # }
        value = cls.stack.pop()
        if cls.api.Py_IsNone(value):
            cls.memory.dec_ref_no_dealloc(value)
            cls.flow.jump_by(oparg)
        else:
            cls.memory.dec_ref(value)
        cls.flow.dispatch()
