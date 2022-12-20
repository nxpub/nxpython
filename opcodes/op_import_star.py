# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpImportStar(BaseOpCode):
    """
    Loads all symbols not starting with '_' directly from the module TOS to
    the local namespace. The module is popped after loading all names. This
    opcode implements from module import *.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_STAR
    """
    OPCODE_NAME = 'IMPORT_STAR'
    OPCODE_VALUE = 84

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(IMPORT_STAR) {
        #     PyObject *from = POP(), *locals;
        #     int err;
        #     if (_PyFrame_FastToLocalsWithError(frame) < 0) {
        #         Py_DECREF(from);
        #         goto error;
        #     }

        #     locals = LOCALS();
        #     if (locals == NULL) {
        #         _PyErr_SetString(tstate, PyExc_SystemError,
        #                          "no locals found during 'import *'");
        #         Py_DECREF(from);
        #         goto error;
        #     }
        #     err = import_all_from(tstate, locals, from);
        #     _PyFrame_LocalsToFast(frame, 0);
        #     Py_DECREF(from);
        #     if (err != 0)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
