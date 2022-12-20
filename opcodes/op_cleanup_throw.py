# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCleanupThrow(BaseOpCode):
    """
    Handles an exception raised during a throw() or
    close() call through the current frame.  If TOS is an
    instance of StopIteration, pop three values from the stack and push
    its value member.  Otherwise, re-raise TOS.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-CLEANUP_THROW
    """
    OPCODE_NAME = 'CLEANUP_THROW'
    OPCODE_VALUE = 55

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CLEANUP_THROW) {
        #     assert(throwflag);
        #     PyObject *exc_value = TOP();
        #     assert(exc_value && PyExceptionInstance_Check(exc_value));
        #     if (PyErr_GivenExceptionMatches(exc_value, PyExc_StopIteration)) {
        #         PyObject *value = ((PyStopIterationObject *)exc_value)->value;
        #         Py_INCREF(value);
        #         Py_DECREF(POP());  // The StopIteration.
        #         Py_DECREF(POP());  // The last sent value.
        #         Py_DECREF(POP());  // The delegated sub-iterator.
        #         PUSH(value);
        #     }
        #     else {
        #         PyObject *exc_type = Py_NewRef(Py_TYPE(exc_value));
        #         PyObject *exc_traceback = PyException_GetTraceback(exc_value);
        #         _PyErr_Restore(tstate, exc_type, Py_NewRef(exc_value), exc_traceback);
        #         goto exception_unwind;
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
