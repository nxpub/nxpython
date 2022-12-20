# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpDeleteSubscr(BaseOpCode):
    """
    Implements del TOS1[TOS].

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_SUBSCR
    """
    OPCODE_NAME = 'DELETE_SUBSCR'
    OPCODE_VALUE = 61

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, container, sub) -> None:
        # TARGET(DELETE_SUBSCR) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *container = PEEK(2);
        #     /* del container[sub] */
        #     int err = PyObject_DelItem(container, sub);
        #     Py_DECREF(container);
        #     Py_DECREF(sub);
        #     if (err) goto pop_2_error;
        #     STACK_SHRINK(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
