# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpJumpIfTrueOrPop(OpCode):
    """
    If TOS is true, increments the bytecode counter by delta and leaves TOS on the
    stack.  Otherwise (TOS is false), TOS is popped.
    
    New in version 3.1.
    
    Changed in version 3.11: The oparg is now a relative delta rather than an absolute target.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_IF_TRUE_OR_POP
    """
    name = 'JUMP_IF_TRUE_OR_POP'
    value = 112

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: JUMP_IF_TRUE_OR_POP stack effect depends on jump flag
        # inst(JUMP_IF_TRUE_OR_POP) {
        #     PyObject *cond = TOP();
        #     int err;
        #     if (Py_IsFalse(cond)) {
        #         STACK_SHRINK(1);
        #         _Py_DECREF_NO_DEALLOC(cond);
        #     }
        #     else if (Py_IsTrue(cond)) {
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         err = PyObject_IsTrue(cond);
        #         if (err > 0) {
        #             JUMPBY(oparg);
        #         }
        #         else if (err == 0) {
        #             STACK_SHRINK(1);
        #             Py_DECREF(cond);
        #         }
        #         else {
        #             goto error;
        #         }
        #     }
        # }
        cond = cls.stack.top()
        if cls.api.Py_IsFalse(cond):
            cls.stack.shrink(1)
            cls.memory.dec_ref_no_dealloc(cond)
        elif cls.api.Py_IsTrue(cond):
            cls.flow.jump_by(oparg)
        else:
            err = cls.api.PyObject_IsTrue(cond)
            if err > 0:
                cls.flow.jump_by(oparg)
            elif err == 0:
                cls.stack.shrink(1)
                cls.memory.dec_ref(cond)
            else:
                cls.flow.error()
        cls.flow.dispatch()
