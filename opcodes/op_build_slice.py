# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBuildSlice(BaseOpCode):
    """
    Pushes a slice object on the stack.  argc must be 2 or 3.  If it is 2,
    slice(TOS1, TOS) is pushed; if it is 3, slice(TOS2, TOS1, TOS) is
    pushed. See the slice() built-in function for more information.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_SLICE
    """
    OPCODE_NAME = 'BUILD_SLICE'
    OPCODE_VALUE = 133

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_SLICE) {
        #     PyObject *start, *stop, *step, *slice;
        #     if (oparg == 3)
        #         step = POP();
        #     else
        #         step = NULL;
        #     stop = POP();
        #     start = TOP();
        #     slice = PySlice_New(start, stop, step);
        #     Py_DECREF(start);
        #     Py_DECREF(stop);
        #     Py_XDECREF(step);
        #     SET_TOP(slice);
        #     if (slice == NULL)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
