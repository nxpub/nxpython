# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteSubscr(OpCode):
    """
    Implements del TOS1[TOS].

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_SUBSCR
    """
    name = 'DELETE_SUBSCR'
    value = 61

    @classmethod
    def logic(cls) -> None:
        # inst(DELETE_SUBSCR, (container, sub --)) {
        #     /* del container[sub] */
        #     int err = PyObject_DelItem(container, sub);
        #     DECREF_INPUTS();
        #     ERROR_IF(err, error);
        # }
        sub = cls.stack.peek(1)
        container = cls.stack.peek(2)
        # del container[sub] 
        err = cls.api.PyObject_DelItem(container, sub)
        cls.memory.dec_ref(container)
        cls.memory.dec_ref(sub)
        cls.flow.error_if(err, 2)
        cls.stack.shrink(2)
        cls.flow.dispatch()
