# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildList(OpCode):
    """
    Works as BUILD_TUPLE, but creates a list.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_LIST
    """
    name = 'BUILD_LIST'
    value = 103

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- __0)
        # inst(BUILD_LIST) {
        #     PyObject *list =  PyList_New(oparg);
        #     if (list == NULL)
        #         goto error;
        #     while (--oparg >= 0) {
        #         PyObject *item = POP();
        #         PyList_SET_ITEM(list, oparg, item);
        #     }
        #     PUSH(list);
        # }
        list = cls.api.PyList_New(oparg)
        if list == None:
            cls.flow.error()
        for oparg in range(oparg - 1, -1, -1):
            item = cls.stack.pop()
            cls.api.PyList_SET_ITEM(list, oparg, item)
        cls.stack.push(list)
        cls.flow.dispatch()
