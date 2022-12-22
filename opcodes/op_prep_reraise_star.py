# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPrepReraiseStar(OpCode):
    """
    Combines the raised and reraised exceptions list from TOS, into an exception
    group to propagate from a try-except* block. Uses the original exception
    group from TOS1 to reconstruct the structure of reraised exceptions. Pops
    two items from the stack and pushes the exception to reraise or None
    if there isn’t one.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-PREP_RERAISE_STAR
    """
    OPCODE_NAME = 'PREP_RERAISE_STAR'
    OPCODE_VALUE = 88

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(PREP_RERAISE_STAR) {
        #     PyObject *excs = POP();
        #     assert(PyList_Check(excs));
        #     PyObject *orig = POP();

        #     PyObject *val = _PyExc_PrepReraiseStar(orig, excs);
        #     Py_DECREF(excs);
        #     Py_DECREF(orig);

        #     if (val == NULL) {
        #         goto error;
        #     }

        #     PUSH(val);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
