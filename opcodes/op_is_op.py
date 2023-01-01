# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpIsOp(OpCode):
    """
    Performs is comparison, or is not if invert is 1.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-IS_OP
    """
    name = 'IS_OP'
    value = 117

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(IS_OP, (left, right -- b)) {
        #     int res = Py_Is(left, right) ^ oparg;
        #     DECREF_INPUTS();
        #     b = Py_NewRef(res ? Py_True : Py_False);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        res = cls.api.Py_Is(left, right) ^ oparg
        cls.memory.dec_ref(left)
        cls.memory.dec_ref(right)
        b = cls.api.Py_NewRef(cls.api.Py_True if res else cls.api.Py_False)
        cls.stack.shrink(1)
        cls.stack.poke(1, b)
        cls.flow.dispatch()
