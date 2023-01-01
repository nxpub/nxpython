# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPopJumpIfFalse(OpCode):
    """
    If TOS is false, increments the bytecode counter by delta.  TOS is popped.
    
    Changed in version 3.11: The oparg is now a relative delta rather than an absolute target.
    This opcode is a pseudo-instruction, replaced in final bytecode by
    the directed versions (forward/backward).
    
    Changed in version 3.12: This is no longer a pseudo-instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_JUMP_IF_FALSE
    """
    name = 'POP_JUMP_IF_FALSE'
    value = 114

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__0 -- )
        # inst(POP_JUMP_IF_FALSE) {
        #     PyObject *cond = POP();
        #     if (Py_IsTrue(cond)) {
        #         _Py_DECREF_NO_DEALLOC(cond);
        #     }
        #     else if (Py_IsFalse(cond)) {
        #         _Py_DECREF_NO_DEALLOC(cond);
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         int err = PyObject_IsTrue(cond);
        #         Py_DECREF(cond);
        #         if (err > 0)
        #             ;
        #         else if (err == 0) {
        #             JUMPBY(oparg);
        #         }
        #         else
        #             goto error;
        #     }
        # }
        cond = cls.stack.pop()
        if cls.api.Py_IsTrue(cond):
            cls.memory.dec_ref_no_dealloc(cond)
        elif cls.api.Py_IsFalse(cond):
            cls.memory.dec_ref_no_dealloc(cond)
            cls.flow.jump_by(oparg)
        else:
            err = cls.api.PyObject_IsTrue(cond)
            cls.memory.dec_ref(cond)
            if err > 0:
                
            elif err == 0:
                cls.flow.jump_by(oparg)
            else:
                cls.flow.error()
        cls.flow.dispatch()
