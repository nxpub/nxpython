# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadFastLoadConst(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_FAST__LOAD_CONST'
    value = 121

    @classmethod
    def logic(cls, oparg: int) -> None:
        # super(LOAD_FAST__LOAD_CONST) = LOAD_FAST + LOAD_CONST;
        raise NotImplementedError
