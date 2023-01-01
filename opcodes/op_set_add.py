# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpSetAdd(OpCode):
    """
    Calls set.add(TOS1[-i], TOS).  Used to implement set comprehensions.

    https://docs.python.org/3.12/library/dis.html#opcode-SET_ADD
    """
    name = 'SET_ADD'
    value = 146

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // Alternative: (set, unused[oparg], v -- set, unused[oparg])
        # inst(SET_ADD, (v --)) {
        #     PyObject *set = PEEK(oparg + 1);  // +1 to account for v staying on stack
        #     int err = PySet_Add(set, v);
        #     Py_DECREF(v);
        #     ERROR_IF(err, error);
        #     PREDICT(JUMP_BACKWARD);
        # }
        v = cls.stack.peek(1)
        set = cls.stack.peek(oparg + 1)  # +1 to account for v staying on stack
        err = cls.api.PySet_Add(set, v)
        cls.memory.dec_ref(v)
        cls.flow.error_if(err, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
