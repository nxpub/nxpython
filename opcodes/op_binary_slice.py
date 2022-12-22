# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinarySlice(OpCode):
    """
    Implements TOS = TOS2[TOS1:TOS].
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_SLICE
    """
    OPCODE_NAME = 'BINARY_SLICE'
    OPCODE_VALUE = 26

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, container, start, stop) -> None:
        # TARGET(BINARY_SLICE) {
        #     PyObject *stop = PEEK(1);
        #     PyObject *start = PEEK(2);
        #     PyObject *container = PEEK(3);
        #     PyObject *res;
        #     PyObject *slice = _PyBuildSlice_ConsumeRefs(start, stop);
        #     // Can't use ERROR_IF() here, because we haven't
        #     // DECREF'ed container yet, and we still own slice.
        #     if (slice == NULL) {
        #         res = NULL;
        #     }
        #     else {
        #         res = PyObject_GetItem(container, slice);
        #         Py_DECREF(slice);
        #     }
        #     Py_DECREF(container);
        #     if (res == NULL) goto pop_3_error;
        #     STACK_SHRINK(2);
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
