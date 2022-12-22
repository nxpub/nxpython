# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpDeleteName(OpCode):
    """
    Implements del name, where namei is the index into co_names
    attribute of the code object.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_NAME
    """
    OPCODE_NAME = 'DELETE_NAME'
    OPCODE_VALUE = 91

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DELETE_NAME) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *ns = LOCALS();
        #     int err;
        #     if (ns == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals when deleting %R", name);
        #         goto error;
        #     }
        #     err = PyObject_DelItem(ns, name);
        #     // Can't use ERROR_IF here.
        #     if (err != 0) {
        #         format_exc_check_arg(tstate, PyExc_NameError,
        #                              NAME_ERROR_MSG,
        #                              name);
        #         goto error;
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
