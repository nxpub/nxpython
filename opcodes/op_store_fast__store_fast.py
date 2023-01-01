# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreFastStoreFast(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'STORE_FAST__STORE_FAST'
    value = 161

    @classmethod
    def logic(cls, oparg: int) -> None:
        # super(STORE_FAST__STORE_FAST) = STORE_FAST + STORE_FAST;
        raise NotImplementedError
