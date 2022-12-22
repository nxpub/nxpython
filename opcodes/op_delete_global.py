# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpDeleteGlobal(OpCode):
    """
    Works as DELETE_NAME, but deletes a global name.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_GLOBAL
    """
    OPCODE_NAME = 'DELETE_GLOBAL'
    OPCODE_VALUE = 98

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DELETE_GLOBAL) {
        #     PyObject *name = GETITEM(names, oparg);
        #     int err;
        #     err = PyDict_DelItem(GLOBALS(), name);
        #     // Can't use ERROR_IF here.
        #     if (err != 0) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #             format_exc_check_arg(tstate, PyExc_NameError,
        #                                  NAME_ERROR_MSG, name);
        #         }
        #         goto error;
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
