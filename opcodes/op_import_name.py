# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpImportName(BaseOpCode):
    """
    Imports the module co_names[namei].  TOS and TOS1 are popped and provide
    the fromlist and level arguments of __import__().  The module
    object is pushed onto the stack.  The current namespace is not affected: for
    a proper import statement, a subsequent STORE_FAST instruction
    modifies the namespace.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_NAME
    """
    OPCODE_NAME = 'IMPORT_NAME'
    OPCODE_VALUE = 108

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(IMPORT_NAME) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *fromlist = POP();
        #     PyObject *level = TOP();
        #     PyObject *res;
        #     res = import_name(tstate, frame, name, fromlist, level);
        #     Py_DECREF(level);
        #     Py_DECREF(fromlist);
        #     SET_TOP(res);
        #     if (res == NULL)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
