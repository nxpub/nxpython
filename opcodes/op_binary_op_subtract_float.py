# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpSubtractFloat(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_SUBTRACT_FLOAT'
    value = 16

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_SUBTRACT_FLOAT, (unused/1, left, right -- sub)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyFloat_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(!PyFloat_CheckExact(right), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     double dsub = ((PyFloatObject *)left)->ob_fval - ((PyFloatObject *)right)->ob_fval;
        #     sub = PyFloat_FromDouble(dsub);
        #     _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc);
        #     ERROR_IF(sub == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyFloat_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(not cls.api.PyFloat_CheckExact(right), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        dsub = (left).ob_fval - (right).ob_fval
        sub = cls.api.PyFloat_FromDouble(dsub)
        cls.memory.dec_ref_specialized(right, cls.api.private.PyFloat_ExactDealloc)
        cls.memory.dec_ref_specialized(left, cls.api.private.PyFloat_ExactDealloc)
        cls.flow.error_if(sub == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, sub)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
