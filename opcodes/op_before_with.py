# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBeforeWith(OpCode):
    """
    This opcode performs several operations before a with block starts.  First,
    it loads __exit__() from the context manager and pushes it onto
    the stack for later use by WITH_EXCEPT_START.  Then,
    __enter__() is called. Finally, the result of calling the
    __enter__() method is pushed onto the stack.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-BEFORE_WITH
    """
    OPCODE_NAME = 'BEFORE_WITH'
    OPCODE_VALUE = 53

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BEFORE_WITH) {
        #     PyObject *mgr = TOP();
        #     PyObject *res;
        #     PyObject *enter = _PyObject_LookupSpecial(mgr, &_Py_ID(__enter__));
        #     if (enter == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "context manager protocol",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         goto error;
        #     }
        #     PyObject *exit = _PyObject_LookupSpecial(mgr, &_Py_ID(__exit__));
        #     if (exit == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "context manager protocol "
        #                           "(missed __exit__ method)",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         Py_DECREF(enter);
        #         goto error;
        #     }
        #     SET_TOP(exit);
        #     Py_DECREF(mgr);
        #     res = _PyObject_CallNoArgs(enter);
        #     Py_DECREF(enter);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     PUSH(res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
