# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadConstLoadFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_CONST__LOAD_FAST'
    value = 113

    @classmethod
    def logic(cls, oparg: int) -> None:
        # super(LOAD_CONST__LOAD_FAST) = LOAD_CONST + LOAD_FAST;
        raise NotImplementedError
