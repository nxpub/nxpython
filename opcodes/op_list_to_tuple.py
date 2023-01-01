# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpListToTuple(OpCode):
    """
    Pops a list from the stack and pushes a tuple containing the same values.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_TO_TUPLE
    """
    name = 'LIST_TO_TUPLE'
    value = 82

    @classmethod
    def logic(cls) -> None:
        # inst(LIST_TO_TUPLE, (list -- tuple)) {
        #     tuple = PyList_AsTuple(list);
        #     DECREF_INPUTS();
        #     ERROR_IF(tuple == NULL, error);
        # }
        list = cls.stack.peek(1)
        tuple = cls.api.PyList_AsTuple(list)
        cls.memory.dec_ref(list)
        cls.flow.error_if(tuple == None, 1)
        cls.stack.poke(1, tuple)
        cls.flow.dispatch()
