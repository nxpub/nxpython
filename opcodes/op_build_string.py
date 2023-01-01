# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildString(OpCode):
    """
    Concatenates count strings from the stack and pushes the resulting string
    onto the stack.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_STRING
    """
    name = 'BUILD_STRING'
    value = 157

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- __0)
        # inst(BUILD_STRING) {
        #     PyObject *str;
        #     str = _PyUnicode_JoinArray(&_Py_STR(empty),
        #                                stack_pointer - oparg, oparg);
        #     if (str == NULL)
        #         goto error;
        #     while (--oparg >= 0) {
        #         PyObject *item = POP();
        #         Py_DECREF(item);
        #     }
        #     PUSH(str);
        # }
        str = cls.api.private.PyUnicode_JoinArray(cls.api.private.Py_STR(empty),
                                   cls.stack - oparg, oparg)
        if str == None:
            cls.flow.error()
        for oparg in range(oparg - 1, -1, -1):
            item = cls.stack.pop()
            cls.memory.dec_ref(item)
        cls.stack.push(str)
        cls.flow.dispatch()
