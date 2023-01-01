# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpListAppend(OpCode):
    """
    Calls list.append(TOS1[-i], TOS).  Used to implement list comprehensions.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_APPEND
    """
    name = 'LIST_APPEND'
    value = 145

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // Alternative: (list, unused[oparg], v -- list, unused[oparg])
        # inst(LIST_APPEND, (v --)) {
        #     PyObject *list = PEEK(oparg + 1);  // +1 to account for v staying on stack
        #     ERROR_IF(_PyList_AppendTakeRef((PyListObject *)list, v) < 0, error);
        #     PREDICT(JUMP_BACKWARD);
        # }
        v = cls.stack.peek(1)
        list = cls.stack.peek(oparg + 1)  # +1 to account for v staying on stack
        cls.flow.error_if(cls.api.private.PyList_AppendTakeRef(list, v) < 0, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
