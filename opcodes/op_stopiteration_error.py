# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStopiterationError(BaseOpCode):
    """
    Handles a StopIteration raised in a generator or coroutine.
    If TOS is an instance of StopIteration, or StopAsyncIteration
    replace it with a RuntimeError.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-STOPITERATION_ERROR
    """
    OPCODE_NAME = 'STOPITERATION_ERROR'
    OPCODE_VALUE = 63

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(STOPITERATION_ERROR) {
        #     assert(frame->owner == FRAME_OWNED_BY_GENERATOR);
        #     PyObject *exc = TOP();
        #     assert(PyExceptionInstance_Check(exc));
        #     const char *msg = NULL;
        #     if (PyErr_GivenExceptionMatches(exc, PyExc_StopIteration)) {
        #         msg = "generator raised StopIteration";
        #         if (frame->f_code->co_flags & CO_ASYNC_GENERATOR) {
        #             msg = "async generator raised StopIteration";
        #         }
        #         else if (frame->f_code->co_flags & CO_COROUTINE) {
        #             msg = "coroutine raised StopIteration";
        #         }
        #     }
        #     else if ((frame->f_code->co_flags & CO_ASYNC_GENERATOR) &&
        #             PyErr_GivenExceptionMatches(exc, PyExc_StopAsyncIteration))
        #     {
        #         /* code in `gen` raised a StopAsyncIteration error:
        #         raise a RuntimeError.
        #         */
        #         msg = "async generator raised StopAsyncIteration";
        #     }
        #     if (msg != NULL) {
        #         PyObject *message = _PyUnicode_FromASCII(msg, strlen(msg));
        #         if (message == NULL) {
        #             goto error;
        #         }
        #         PyObject *error = PyObject_CallOneArg(PyExc_RuntimeError, message);
        #         if (error == NULL) {
        #             Py_DECREF(message);
        #             goto error;
        #         }
        #         assert(PyExceptionInstance_Check(error));
        #         SET_TOP(error);
        #         PyException_SetCause(error, Py_NewRef(exc));
        #         // Steal exc reference, rather than Py_NewRef+Py_DECREF
        #         PyException_SetContext(error, exc);
        #         Py_DECREF(message);
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
