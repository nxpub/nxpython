# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpMapAdd(OpCode):
    """
    Calls dict.__setitem__(TOS1[-i], TOS1, TOS).  Used to implement dict
    comprehensions.
    
    New in version 3.1.
    
    Changed in version 3.8: Map value is TOS and map key is TOS1. Before, those were reversed.

    https://docs.python.org/3.12/library/dis.html#opcode-MAP_ADD
    """
    name = 'MAP_ADD'
    value = 147

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(MAP_ADD, (key, value --)) {
        #     PyObject *dict = PEEK(oparg + 2);  // key, value are still on the stack
        #     assert(PyDict_CheckExact(dict));
        #     /* dict[key] = value */
        #     // Do not DECREF INPUTS because the function steals the references
        #     ERROR_IF(_PyDict_SetItem_Take2((PyDictObject *)dict, key, value) != 0, error);
        #     PREDICT(JUMP_BACKWARD);
        # }
        value = cls.stack.peek(1)
        key = cls.stack.peek(2)
        dict = cls.stack.peek(oparg + 2)  # key, value are still on the stack
        # assert(PyDict_CheckExact(dict))
        # dict[key] = value 
        # Do not DECREF INPUTS because the function steals the references
        cls.flow.error_if(cls.api.private.PyDict_SetItem_Take2(dict, key, value) != 0, 2)
        cls.stack.shrink(2)
        cls.flow.dispatch()
