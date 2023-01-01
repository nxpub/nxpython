# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnaryInvert(OpCode):
    """
    Implements TOS = ~TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_INVERT
    """
    name = 'UNARY_INVERT'
    value = 15

    @classmethod
    def logic(cls) -> None:
        # inst(UNARY_INVERT, (value -- res)) {
        #     res = PyNumber_Invert(value);
        #     DECREF_INPUTS();
        #     ERROR_IF(res == NULL, error);
        # }
        value = cls.stack.peek(1)
        res = cls.api.PyNumber_Invert(value)
        cls.memory.dec_ref(value)
        cls.flow.error_if(res == None, 1)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
