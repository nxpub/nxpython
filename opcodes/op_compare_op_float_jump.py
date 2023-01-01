# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCompareOpFloatJump(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'COMPARE_OP_FLOAT_JUMP'
    value = 56

    @classmethod
    def logic(cls) -> None:
        # // We're praying that the compiler optimizes the flags manipuations.
        # super(COMPARE_OP_FLOAT_JUMP) = _COMPARE_OP_FLOAT + _JUMP_IF;
        raise NotImplementedError
