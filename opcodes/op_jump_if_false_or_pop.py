# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpJumpIfFalseOrPop(OpCode):
    """
    If TOS is false, increments the bytecode counter by delta and leaves TOS on the
    stack.  Otherwise (TOS is true), TOS is popped.
    
    New in version 3.1.
    
    Changed in version 3.11: The oparg is now a relative delta rather than an absolute target.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_IF_FALSE_OR_POP
    """
    name = 'JUMP_IF_FALSE_OR_POP'
    value = 111

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: JUMP_IF_FALSE_OR_POP stack effect depends on jump flag
        # inst(JUMP_IF_FALSE_OR_POP) {
        #     PyObject *cond = TOP();
        #     int err;
        #     if (Py_IsTrue(cond)) {
        #         STACK_SHRINK(1);
        #         _Py_DECREF_NO_DEALLOC(cond);
        #     }
        #     else if (Py_IsFalse(cond)) {
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         err = PyObject_IsTrue(cond);
        #         if (err > 0) {
        #             STACK_SHRINK(1);
        #             Py_DECREF(cond);
        #         }
        #         else if (err == 0) {
        #             JUMPBY(oparg);
        #         }
        #         else {
        #             goto error;
        #         }
        #     }
        # }
        cond = cls.stack.top()
        if cls.api.Py_IsTrue(cond):
            cls.stack.shrink(1)
            cls.memory.dec_ref_no_dealloc(cond)
        elif cls.api.Py_IsFalse(cond):
            cls.flow.jump_by(oparg)
        else:
            err = cls.api.PyObject_IsTrue(cond)
            if err > 0:
                cls.stack.shrink(1)
                cls.memory.dec_ref(cond)
            elif err == 0:
                cls.flow.jump_by(oparg)
            else:
                cls.flow.error()
        cls.flow.dispatch()
