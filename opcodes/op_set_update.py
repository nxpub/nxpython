# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpSetUpdate(OpCode):
    """
    Calls set.update(TOS1[-i], TOS).  Used to build sets.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-SET_UPDATE
    """
    name = 'SET_UPDATE'
    value = 163

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(SET_UPDATE, (iterable --)) {
        #     PyObject *set = PEEK(oparg + 1);  // iterable is still on the stack
        #     int err = _PySet_Update(set, iterable);
        #     DECREF_INPUTS();
        #     ERROR_IF(err < 0, error);
        # }
        iterable = cls.stack.peek(1)
        set = cls.stack.peek(oparg + 1)  # iterable is still on the stack
        err = cls.api.private.PySet_Update(set, iterable)
        cls.memory.dec_ref(iterable)
        cls.flow.error_if(err < 0, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
