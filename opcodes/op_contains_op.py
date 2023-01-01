# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpContainsOp(OpCode):
    """
    Performs in comparison, or not in if invert is 1.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-CONTAINS_OP
    """
    name = 'CONTAINS_OP'
    value = 118

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(CONTAINS_OP, (left, right -- b)) {
        #     int res = PySequence_Contains(right, left);
        #     DECREF_INPUTS();
        #     ERROR_IF(res < 0, error);
        #     b = Py_NewRef((res^oparg) ? Py_True : Py_False);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        res = cls.api.PySequence_Contains(right, left)
        cls.memory.dec_ref(left)
        cls.memory.dec_ref(right)
        cls.flow.error_if(res < 0, 2)
        b = cls.api.Py_NewRef(cls.api.Py_True if res^oparg) else cls.api.Py_False)
        cls.stack.shrink(1)
        cls.stack.poke(1, b)
        cls.flow.dispatch()
