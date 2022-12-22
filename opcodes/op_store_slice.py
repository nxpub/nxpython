# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreSlice(OpCode):
    """
    Implements TOS2[TOS1:TOS] = TOS3.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_SLICE
    """
    OPCODE_NAME = 'STORE_SLICE'
    OPCODE_VALUE = 27

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, v, container, start, stop) -> None:
        # TARGET(STORE_SLICE) {
        #     PyObject *stop = PEEK(1);
        #     PyObject *start = PEEK(2);
        #     PyObject *container = PEEK(3);
        #     PyObject *v = PEEK(4);
        #     PyObject *slice = _PyBuildSlice_ConsumeRefs(start, stop);
        #     int err;
        #     if (slice == NULL) {
        #         err = 1;
        #     }
        #     else {
        #         err = PyObject_SetItem(container, slice, v);
        #         Py_DECREF(slice);
        #     }
        #     Py_DECREF(v);
        #     Py_DECREF(container);
        #     if (err) goto pop_4_error;
        #     STACK_SHRINK(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
