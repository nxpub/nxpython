# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCheckExcMatch(OpCode):
    """
    Performs exception matching for except. Tests whether the TOS1 is an exception
    matching TOS. Pops TOS and pushes the boolean result of the test.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-CHECK_EXC_MATCH
    """
    OPCODE_NAME = 'CHECK_EXC_MATCH'
    OPCODE_VALUE = 36

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CHECK_EXC_MATCH) {
        #     PyObject *right = POP();
        #     PyObject *left = TOP();
        #     assert(PyExceptionInstance_Check(left));
        #     if (check_except_type_valid(tstate, right) < 0) {
        #          Py_DECREF(right);
        #          goto error;
        #     }

        #     int res = PyErr_GivenExceptionMatches(left, right);
        #     Py_DECREF(right);
        #     PUSH(Py_NewRef(res ? Py_True : Py_False));
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
