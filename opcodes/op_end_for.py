# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpEndFor(BaseOpCode):
    """
    Removes the top two values from the stack.
    Equivalent to POP_TOP; POP_TOP.
    Used to clean up at the end of loops, hence the name.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-END_FOR
    """
    OPCODE_NAME = 'END_FOR'
    OPCODE_VALUE = 4

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(END_FOR) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     PyObject *_tmp_2 = PEEK(2);
        #     {
        #         PyObject *value = _tmp_1;
        #         Py_DECREF(value);
        #     }
        #     {
        #         PyObject *value = _tmp_2;
        #         Py_DECREF(value);
        #     }
        #     STACK_SHRINK(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
