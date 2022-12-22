# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpLoadName(OpCode):
    """
    Pushes the value associated with co_names[namei] onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_NAME
    """
    OPCODE_NAME = 'LOAD_NAME'
    OPCODE_VALUE = 101

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_NAME) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *locals = LOCALS();
        #     PyObject *v;
        #     if (locals == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals when loading %R", name);
        #         goto error;
        #     }
        #     if (PyDict_CheckExact(locals)) {
        #         v = PyDict_GetItemWithError(locals, name);
        #         if (v != NULL) {
        #             Py_INCREF(v);
        #         }
        #         else if (_PyErr_Occurred(tstate)) {
        #             goto error;
        #         }
        #     }
        #     else {
        #         v = PyObject_GetItem(locals, name);
        #         if (v == NULL) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_KeyError))
        #                 goto error;
        #             _PyErr_Clear(tstate);
        #         }
        #     }
        #     if (v == NULL) {
        #         v = PyDict_GetItemWithError(GLOBALS(), name);
        #         if (v != NULL) {
        #             Py_INCREF(v);
        #         }
        #         else if (_PyErr_Occurred(tstate)) {
        #             goto error;
        #         }
        #         else {
        #             if (PyDict_CheckExact(BUILTINS())) {
        #                 v = PyDict_GetItemWithError(BUILTINS(), name);
        #                 if (v == NULL) {
        #                     if (!_PyErr_Occurred(tstate)) {
        #                         format_exc_check_arg(
        #                                 tstate, PyExc_NameError,
        #                                 NAME_ERROR_MSG, name);
        #                     }
        #                     goto error;
        #                 }
        #                 Py_INCREF(v);
        #             }
        #             else {
        #                 v = PyObject_GetItem(BUILTINS(), name);
        #                 if (v == NULL) {
        #                     if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                         format_exc_check_arg(
        #                                     tstate, PyExc_NameError,
        #                                     NAME_ERROR_MSG, name);
        #                     }
        #                     goto error;
        #                 }
        #             }
        #         }
        #     }
        #     PUSH(v);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
