# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBuildList(OpCode):
    """
    Works as BUILD_TUPLE, but creates a list.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_LIST
    """
    OPCODE_NAME = 'BUILD_LIST'
    OPCODE_VALUE = 103

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_LIST) {
        #     PyObject *list =  PyList_New(oparg);
        #     if (list == NULL)
        #         goto error;
        #     while (--oparg >= 0) {
        #         PyObject *item = POP();
        #         PyList_SET_ITEM(list, oparg, item);
        #     }
        #     PUSH(list);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
