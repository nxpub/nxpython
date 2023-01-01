# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreFastLoadFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_FAST__LOAD_FAST'
    value = 160

    @classmethod
    def logic(cls, oparg: int) -> None:
        # super(STORE_FAST__LOAD_FAST)  = STORE_FAST + LOAD_FAST;
        raise NotImplementedError
