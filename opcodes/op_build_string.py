# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBuildString(BaseOpCode):
    """
    Concatenates count strings from the stack and pushes the resulting string
    onto the stack.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_STRING
    """
    OPCODE_NAME = 'BUILD_STRING'
    OPCODE_VALUE = 157

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_STRING) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
