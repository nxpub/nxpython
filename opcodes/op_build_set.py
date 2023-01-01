# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildSet(OpCode):
    """
    Works as BUILD_TUPLE, but creates a set.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_SET
    """
    name = 'BUILD_SET'
    value = 104

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- __0)
        # inst(BUILD_SET) {
        #     PyObject *set = PySet_New(NULL);
        #     int err = 0;
        #     int i;
        #     if (set == NULL)
        #         goto error;
        #     for (i = oparg; i > 0; i--) {
        #         PyObject *item = PEEK(i);
        #         if (err == 0)
        #             err = PySet_Add(set, item);
        #         Py_DECREF(item);
        #     }
        #     STACK_SHRINK(oparg);
        #     if (err != 0) {
        #         Py_DECREF(set);
        #         goto error;
        #     }
        #     PUSH(set);
        # }
        set = cls.api.PySet_New(None)
        err = 0
        if set == None:
            cls.flow.error()
        for i in range(oparg, 0, -1):
            item = cls.stack.peek(i)
            if err == 0:
                err = cls.api.PySet_Add(set, item)
            cls.memory.dec_ref(item)
        cls.stack.shrink(oparg)
        if err != 0:
            cls.memory.dec_ref(set)
            cls.flow.error()
        cls.stack.push(set)
        cls.flow.dispatch()
