# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCheckExcMatch(OpCode):
    """
    Performs exception matching for except. Tests whether the TOS1 is an exception
    matching TOS. Pops TOS and pushes the boolean result of the test.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-CHECK_EXC_MATCH
    """
    name = 'CHECK_EXC_MATCH'
    value = 36

    @classmethod
    def logic(cls) -> None:
        # inst(CHECK_EXC_MATCH, (left, right -- left, b)) {
        #     assert(PyExceptionInstance_Check(left));
        #     if (check_except_type_valid(tstate, right) < 0) {
        #          DECREF_INPUTS();
        #          ERROR_IF(true, error);
        #     }

        #     int res = PyErr_GivenExceptionMatches(left, right);
        #     DECREF_INPUTS();
        #     b = Py_NewRef(res ? Py_True : Py_False);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(PyExceptionInstance_Check(left))
        if check_except_type_valid(cls.frame.state, right) < 0:
             cls.memory.dec_ref(right)
             cls.flow.error_if(True, 1)

        res = cls.api.PyErr_GivenExceptionMatches(left, right)
        cls.memory.dec_ref(right)
        b = cls.api.Py_NewRef(cls.api.Py_True if res else cls.api.Py_False)
        cls.stack.poke(1, b)
        cls.flow.dispatch()
