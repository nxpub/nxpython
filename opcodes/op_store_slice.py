# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreSlice(OpCode):
    """
    Implements TOS2[TOS1:TOS] = TOS3.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_SLICE
    """
    name = 'STORE_SLICE'
    value = 27

    @classmethod
    def logic(cls) -> None:
        # inst(STORE_SLICE, (v, container, start, stop -- )) {
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
        #     ERROR_IF(err, error);
        # }
        stop = cls.stack.peek(1)
        start = cls.stack.peek(2)
        container = cls.stack.peek(3)
        v = cls.stack.peek(4)
        slice = cls.api.private.PyBuildSlice_ConsumeRefs(start, stop)
        if slice == None:
            err = 1
        else:
            err = cls.api.PyObject_SetItem(container, slice, v)
            cls.memory.dec_ref(slice)
        cls.memory.dec_ref(v)
        cls.memory.dec_ref(container)
        cls.flow.error_if(err, 4)
        cls.stack.shrink(4)
        cls.flow.dispatch()
