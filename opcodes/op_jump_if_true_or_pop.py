# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpJumpIfTrueOrPop(OpCode):
    """
    If TOS is true, increments the bytecode counter by delta and leaves TOS on the
    stack.  Otherwise (TOS is false), TOS is popped.
    
    New in version 3.1.
    
    Changed in version 3.11: The oparg is now a relative delta rather than an absolute target.

    https://docs.python.org/3.12/library/dis.html#opcode-JUMP_IF_TRUE_OR_POP
    """
    OPCODE_NAME = 'JUMP_IF_TRUE_OR_POP'
    OPCODE_VALUE = 112

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(JUMP_IF_TRUE_OR_POP) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
