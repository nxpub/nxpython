# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPopJumpIfTrue(OpCode):
    """
    If TOS is true, increments the bytecode counter by delta.  TOS is popped.
    
    Changed in version 3.11: The oparg is now a relative delta rather than an absolute target.
    This opcode is a pseudo-instruction, replaced in final bytecode by
    the directed versions (forward/backward).
    
    Changed in version 3.12: This is no longer a pseudo-instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-POP_JUMP_IF_TRUE
    """
    OPCODE_NAME = 'POP_JUMP_IF_TRUE'
    OPCODE_VALUE = 115

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(POP_JUMP_IF_TRUE) {
        #     PyObject *cond = POP();
        #     if (Py_IsFalse(cond)) {
        #         _Py_DECREF_NO_DEALLOC(cond);
        #     }
        #     else if (Py_IsTrue(cond)) {
        #         _Py_DECREF_NO_DEALLOC(cond);
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         int err = PyObject_IsTrue(cond);
        #         Py_DECREF(cond);
        #         if (err > 0) {
        #             JUMPBY(oparg);
        #         }
        #         else if (err == 0)
        #             ;
        #         else
        #             goto error;
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
