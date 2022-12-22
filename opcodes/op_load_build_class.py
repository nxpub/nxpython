# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpLoadBuildClass(OpCode):
    """
    Pushes builtins.__build_class__() onto the stack.  It is later called
    to construct a class.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_BUILD_CLASS
    """
    OPCODE_NAME = 'LOAD_BUILD_CLASS'
    OPCODE_VALUE = 71

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_BUILD_CLASS) {
        #     PyObject *bc;
        #     if (PyDict_CheckExact(BUILTINS())) {
        #         bc = _PyDict_GetItemWithError(BUILTINS(),
        #                                       &_Py_ID(__build_class__));
        #         if (bc == NULL) {
        #             if (!_PyErr_Occurred(tstate)) {
        #                 _PyErr_SetString(tstate, PyExc_NameError,
        #                                  "__build_class__ not found");
        #             }
        #             goto error;
        #         }
        #         Py_INCREF(bc);
        #     }
        #     else {
        #         bc = PyObject_GetItem(BUILTINS(), &_Py_ID(__build_class__));
        #         if (bc == NULL) {
        #             if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError))
        #                 _PyErr_SetString(tstate, PyExc_NameError,
        #                                  "__build_class__ not found");
        #             goto error;
        #         }
        #     }
        #     PUSH(bc);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
