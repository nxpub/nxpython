# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadFastLoadFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_FAST__LOAD_FAST'
    value = 141

    @classmethod
    def logic(cls, oparg: int) -> None:
        # super(LOAD_FAST__LOAD_FAST) = LOAD_FAST + LOAD_FAST;
        raise NotImplementedError
