# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMatchClass(BaseOpCode):
    """
    TOS is a tuple of keyword attribute names, TOS1 is the class being matched
    against, and TOS2 is the match subject.  count is the number of positional
    sub-patterns.
    
    Pop TOS, TOS1, and TOS2.  If TOS2 is an instance of TOS1 and has the
    positional and keyword attributes required by count and TOS, push a tuple
    of extracted attributes.  Otherwise, push None.
    
    New in version 3.10.
    
    Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating
    success (True) or failure (False).

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_CLASS
    """
    OPCODE_NAME = 'MATCH_CLASS'
    OPCODE_VALUE = 152

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MATCH_CLASS) {
        #     // Pop TOS and TOS1. Set TOS to a tuple of attributes on success, or
        #     // None on failure.
        #     PyObject *names = POP();
        #     PyObject *type = POP();
        #     PyObject *subject = TOP();
        #     assert(PyTuple_CheckExact(names));
        #     PyObject *attrs = match_class(tstate, subject, type, oparg, names);
        #     Py_DECREF(names);
        #     Py_DECREF(type);
        #     if (attrs) {
        #         // Success!
        #         assert(PyTuple_CheckExact(attrs));
        #         SET_TOP(attrs);
        #     }
        #     else if (_PyErr_Occurred(tstate)) {
        #         // Error!
        #         goto error;
        #     }
        #     else {
        #         // Failure!
        #         SET_TOP(Py_NewRef(Py_None));
        #     }
        #     Py_DECREF(subject);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
