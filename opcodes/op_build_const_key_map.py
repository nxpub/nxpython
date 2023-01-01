# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildConstKeyMap(OpCode):
    """
    The version of BUILD_MAP specialized for constant keys. Pops the
    top element on the stack which contains a tuple of keys, then starting from
    TOS1, pops count values to form values in the built dictionary.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_CONST_KEY_MAP
    """
    name = 'BUILD_CONST_KEY_MAP'
    value = 156

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- )
        # inst(BUILD_CONST_KEY_MAP) {
        #     PyObject *map;
        #     PyObject *keys = TOP();
        #     if (!PyTuple_CheckExact(keys) ||
        #         PyTuple_GET_SIZE(keys) != (Py_ssize_t)oparg) {
        #         _PyErr_SetString(tstate, PyExc_SystemError,
        #                          "bad BUILD_CONST_KEY_MAP keys argument");
        #         goto error;
        #     }
        #     map = _PyDict_FromItems(
        #             &PyTuple_GET_ITEM(keys, 0), 1,
        #             &PEEK(oparg + 1), 1, oparg);
        #     if (map == NULL) {
        #         goto error;
        #     }

        #     Py_DECREF(POP());
        #     while (oparg--) {
        #         Py_DECREF(POP());
        #     }
        #     PUSH(map);
        # }
        keys = cls.stack.top()
        if not cls.api.PyTuple_CheckExact(keys:||
            cls.api.PyTuple_GET_SIZE(keys) != (cls.api.Py_ssize_t)oparg) {
            cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_SystemError,
                             "bad BUILD_CONST_KEY_MAP keys argument")
            cls.flow.error()
        map = cls.api.private.PyDict_FromItems(
                cls.api.PyTuple_GET_ITEM(keys, 0), 1,
                cls.stack.peek(oparg + 1), 1, oparg)
        if map == None:
            cls.flow.error()

        cls.memory.dec_ref(cls.stack.pop())
        for oparg in range(oparg, 0, -1):
            cls.memory.dec_ref(cls.stack.pop())
        cls.stack.push(map)
        cls.flow.dispatch()
