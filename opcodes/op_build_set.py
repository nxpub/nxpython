# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBuildSet(OpCode):
    """
    Works as BUILD_TUPLE, but creates a set.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_SET
    """
    OPCODE_NAME = 'BUILD_SET'
    OPCODE_VALUE = 104

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_SET) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
