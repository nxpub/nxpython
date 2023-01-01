# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildSlice(OpCode):
    """
    Pushes a slice object on the stack.  argc must be 2 or 3.  If it is 2,
    slice(TOS1, TOS) is pushed; if it is 3, slice(TOS2, TOS1, TOS) is
    pushed. See the slice() built-in function for more information.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_SLICE
    """
    name = 'BUILD_SLICE'
    value = 133

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: BUILD_SLICE has irregular stack effect
        # inst(BUILD_SLICE) {
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
        # }
        start, *stop, *step, *slice
        if oparg == 3:
            step = cls.stack.pop()
        else:
            step = None
        stop = cls.stack.pop()
        start = cls.stack.top()
        slice = cls.api.PySlice_New(start, stop, step)
        cls.memory.dec_ref(start)
        cls.memory.dec_ref(stop)
        cls.memory.dec_ref_x(step)
        cls.stack.set_top(slice)
        if slice == None:
            cls.flow.error()
        cls.flow.dispatch()
