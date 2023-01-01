# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpUnaryNot(OpCode):
    """
    Implements TOS = not TOS.

    https://docs.python.org/3.12/library/dis.html#opcode-UNARY_NOT
    """
    name = 'UNARY_NOT'
    value = 12

    @classmethod
    def logic(cls) -> None:
        # inst(UNARY_NOT, (value -- res)) {
        #     int err = PyObject_IsTrue(value);
        #     DECREF_INPUTS();
        #     ERROR_IF(err < 0, error);
        #     if (err == 0) {
        #         res = Py_True;
        #     }
        #     else {
        #         res = Py_False;
        #     }
        #     Py_INCREF(res);
        # }
        value = cls.stack.peek(1)
        err = cls.api.PyObject_IsTrue(value)
        cls.memory.dec_ref(value)
        cls.flow.error_if(err < 0, 1)
        if err == 0:
            res = cls.api.Py_True
        else:
            res = cls.api.Py_False
        cls.memory.inc_ref(res)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
