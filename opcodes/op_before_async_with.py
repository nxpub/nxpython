# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBeforeAsyncWith(OpCode):
    """
    Resolves __aenter__ and __aexit__ from the object on top of the
    stack.  Pushes __aexit__ and result of __aenter__() to the stack.
    
    New in version 3.5.

    https://docs.python.org/3.12/library/dis.html#opcode-BEFORE_ASYNC_WITH
    """
    OPCODE_NAME = 'BEFORE_ASYNC_WITH'
    OPCODE_VALUE = 52

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BEFORE_ASYNC_WITH) {
        #     PyObject *mgr = TOP();
        #     PyObject *res;
        #     PyObject *enter = _PyObject_LookupSpecial(mgr, &_Py_ID(__aenter__));
        #     if (enter == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "asynchronous context manager protocol",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         goto error;
        #     }
        #     PyObject *exit = _PyObject_LookupSpecial(mgr, &_Py_ID(__aexit__));
        #     if (exit == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'%.200s' object does not support the "
        #                           "asynchronous context manager protocol "
        #                           "(missed __aexit__ method)",
        #                           Py_TYPE(mgr)->tp_name);
        #         }
        #         Py_DECREF(enter);
        #         goto error;
        #     }
        #     SET_TOP(exit);
        #     Py_DECREF(mgr);
        #     res = _PyObject_CallNoArgs(enter);
        #     Py_DECREF(enter);
        #     if (res == NULL)
        #         goto error;
        #     PUSH(res);
        #     PREDICT(GET_AWAITABLE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
