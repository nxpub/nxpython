# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPushNull(OpCode):
    """
    Pushes a NULL to the stack.
    Used in the call sequence to match the NULL pushed by
    LOAD_METHOD for non-method calls.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-PUSH_NULL
    """
    name = 'PUSH_NULL'
    value = 2

    @classmethod
    def logic(cls) -> None:
        # inst(PUSH_NULL, (-- res)) {
        #     res = NULL;
        # }
        res = None
        cls.stack.grow(1)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
