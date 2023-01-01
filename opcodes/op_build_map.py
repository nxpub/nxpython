# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildMap(OpCode):
    """
    Pushes a new dictionary object onto the stack.  Pops 2 * count items
    so that the dictionary holds count entries:
    {..., TOS3: TOS2, TOS1: TOS}.
    
    Changed in version 3.5: The dictionary is created from stack items instead of creating an
    empty dictionary pre-sized to hold count items.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_MAP
    """
    name = 'BUILD_MAP'
    value = 105

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg*2] -- __0)
        # inst(BUILD_MAP) {
        #     PyObject *map = _PyDict_FromItems(
        #             &PEEK(2*oparg), 2,
        #             &PEEK(2*oparg - 1), 2,
        #             oparg);
        #     if (map == NULL)
        #         goto error;

        #     while (oparg--) {
        #         Py_DECREF(POP());
        #         Py_DECREF(POP());
        #     }
        #     PUSH(map);
        # }
        map = cls.api.private.PyDict_FromItems(
                cls.stack.peek(2*oparg), 2,
                cls.stack.peek(2*oparg - 1), 2,
                oparg)
        if map == None:
            cls.flow.error()

        for oparg in range(oparg, 0, -1):
            cls.memory.dec_ref(cls.stack.pop())
            cls.memory.dec_ref(cls.stack.pop())
        cls.stack.push(map)
        cls.flow.dispatch()
