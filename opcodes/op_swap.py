# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpSwap(OpCode):
    """
    Swap TOS with the item at position i.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-SWAP
    """
    name = 'SWAP'
    value = 99

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: ( -- )
        # inst(SWAP) {
        #     assert(oparg != 0);
        #     PyObject *top = TOP();
        #     SET_TOP(PEEK(oparg));
        #     PEEK(oparg) = top;
        # }
        # assert(oparg != 0)
        top = cls.stack.top()
        cls.stack.set_top(cls.stack.peek(oparg))
        cls.stack.peek(oparg) = top
        cls.flow.dispatch()
