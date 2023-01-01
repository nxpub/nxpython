# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAssertionError(OpCode):
    """
    Pushes AssertionError onto the stack.  Used by the assert
    statement.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_ASSERTION_ERROR
    """
    name = 'LOAD_ASSERTION_ERROR'
    value = 74

    @classmethod
    def logic(cls) -> None:
        # inst(LOAD_ASSERTION_ERROR, ( -- value)) {
        #     value = Py_NewRef(PyExc_AssertionError);
        # }
        value = cls.api.Py_NewRef(cls.api.PyExc_AssertionError)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
