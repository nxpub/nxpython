# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpSubtractInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_SUBTRACT_INT'
    value = 17

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_SUBTRACT_INT, (unused/1, left, right -- sub)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyLong_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     sub = _PyLong_Subtract((PyLongObject *)left, (PyLongObject *)right);
        #     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #     ERROR_IF(sub == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(right), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        sub = cls.api.private.PyLong_Subtract(left, right)
        cls.memory.dec_ref_specialized(right, cls.api.PyObject_Free)
        cls.memory.dec_ref_specialized(left, cls.api.PyObject_Free)
        cls.flow.error_if(sub == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, sub)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
