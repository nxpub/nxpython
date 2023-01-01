# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpMultiplyInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_MULTIPLY_INT'
    value = 14

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_MULTIPLY_INT, (unused/1, left, right -- prod)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyLong_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     prod = _PyLong_Multiply((PyLongObject *)left, (PyLongObject *)right);
        #     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #     ERROR_IF(prod == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(right), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        prod = cls.api.private.PyLong_Multiply(left, right)
        cls.memory.dec_ref_specialized(right, cls.api.PyObject_Free)
        cls.memory.dec_ref_specialized(left, cls.api.PyObject_Free)
        cls.flow.error_if(prod == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, prod)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
