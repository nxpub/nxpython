# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinarySlice(OpCode):
    """
    Implements TOS = TOS2[TOS1:TOS].
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-BINARY_SLICE
    """
    name = 'BINARY_SLICE'
    value = 26

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_SLICE, (container, start, stop -- res)) {
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
        #     ERROR_IF(res == NULL, error);
        # }
        stop = cls.stack.peek(1)
        start = cls.stack.peek(2)
        container = cls.stack.peek(3)
        slice = cls.api.private.PyBuildSlice_ConsumeRefs(start, stop)
        # Can't use ERROR_IF() here, because we haven't
        # DECREF'ed container yet, and we still own slice.
        if slice == None:
            res = None
        else:
            res = cls.api.PyObject_GetItem(container, slice)
            cls.memory.dec_ref(slice)
        cls.memory.dec_ref(container)
        cls.flow.error_if(res == None, 3)
        cls.stack.shrink(2)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
