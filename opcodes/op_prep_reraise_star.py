# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


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
    name = 'PREP_RERAISE_STAR'
    value = 88

    @classmethod
    def logic(cls) -> None:
        # inst(PREP_RERAISE_STAR, (orig, excs -- val)) {
        #     assert(PyList_Check(excs));

        #     val = _PyExc_PrepReraiseStar(orig, excs);
        #     DECREF_INPUTS();

        #     ERROR_IF(val == NULL, error);
        # }
        excs = cls.stack.peek(1)
        orig = cls.stack.peek(2)
        # assert(PyList_Check(excs))

        val = cls.api.private.PyExc_PrepReraiseStar(orig, excs)
        cls.memory.dec_ref(orig)
        cls.memory.dec_ref(excs)

        cls.flow.error_if(val == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, val)
        cls.flow.dispatch()
