# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnpackEx(OpCode):
    """
    Implements assignment with a starred target: Unpacks an iterable in TOS into
    individual values, where the total number of values can be smaller than the
    number of items in the iterable: one of the new values will be a list of all
    leftover items.
    
    The low byte of counts is the number of values before the list value, the
    high byte of counts the number of values after it.  The resulting values
    are put onto the stack right-to-left.

    https://docs.python.org/3.12/library/dis.html#opcode-UNPACK_EX
    """
    name = 'UNPACK_EX'
    value = 94

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: UNPACK_EX has irregular stack effect
        # inst(UNPACK_EX) {
        #     int totalargs = 1 + (oparg & 0xFF) + (oparg >> 8);
        #     PyObject *seq = POP();
        #     PyObject **top = stack_pointer + totalargs;
        #     if (!unpack_iterable(tstate, seq, oparg & 0xFF, oparg >> 8, top)) {
        #         Py_DECREF(seq);
        #         goto error;
        #     }
        #     STACK_GROW(totalargs);
        #     Py_DECREF(seq);
        # }
        totalargs = 1 + (oparg & 0xFF) + (oparg >> 8)
        seq = cls.stack.pop()
        top = cls.stack + totalargs
        if not unpack_iterable(cls.frame.state, seq, oparg & 0xFF, oparg >> 8, top):
            cls.memory.dec_ref(seq)
            cls.flow.error()
        cls.stack.grow(totalargs)
        cls.memory.dec_ref(seq)
        cls.flow.dispatch()
