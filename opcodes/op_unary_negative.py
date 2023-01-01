# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnaryNegative(OpCode):
    """
    Implements TOS = -TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_NEGATIVE
    """
    name = 'UNARY_NEGATIVE'
    value = 11

    @classmethod
    def logic(cls) -> None:
        # inst(UNARY_NEGATIVE, (value -- res)) {
        #     res = PyNumber_Negative(value);
        #     DECREF_INPUTS();
        #     ERROR_IF(res == NULL, error);
        # }
        value = cls.stack.peek(1)
        res = cls.api.PyNumber_Negative(value)
        cls.memory.dec_ref(value)
        cls.flow.error_if(res == None, 1)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
