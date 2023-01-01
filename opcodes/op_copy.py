# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCopy(OpCode):
    """
    Push the i-th item to the top of the stack. The item is not removed from its
    original location.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-COPY
    """
    name = 'COPY'
    value = 120

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: ( -- __0)
        # inst(COPY) {
        #     assert(oparg != 0);
        #     PyObject *peek = PEEK(oparg);
        #     PUSH(Py_NewRef(peek));
        # }
        # assert(oparg != 0)
        peek = cls.stack.peek(oparg)
        cls.stack.push(cls.api.Py_NewRef(peek))
        cls.flow.dispatch()
