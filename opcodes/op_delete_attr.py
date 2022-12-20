# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpDeleteAttr(BaseOpCode):
    """
    Implements del TOS.name, using namei as index into co_names.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_ATTR
    """
    OPCODE_NAME = 'DELETE_ATTR'
    OPCODE_VALUE = 96

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, owner) -> None:
        # TARGET(DELETE_ATTR) {
        #     PyObject *owner = PEEK(1);
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyObject_SetAttr(owner, name, (PyObject *)NULL);
        #     Py_DECREF(owner);
        #     if (err) goto pop_1_error;
        #     STACK_SHRINK(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
