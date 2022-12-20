# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreGlobal(BaseOpCode):
    """
    Works as STORE_NAME, but stores the name as a global.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_GLOBAL
    """
    OPCODE_NAME = 'STORE_GLOBAL'
    OPCODE_VALUE = 97

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, v) -> None:
        # TARGET(STORE_GLOBAL) {
        #     PyObject *v = PEEK(1);
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyDict_SetItem(GLOBALS(), name, v);
        #     Py_DECREF(v);
        #     if (err) goto pop_1_error;
        #     STACK_SHRINK(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
