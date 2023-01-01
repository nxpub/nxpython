# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpAddFloat(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_ADD_FLOAT'
    value = 5

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_ADD_FLOAT, (unused/1, left, right -- sum)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyFloat_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     double dsum = ((PyFloatObject *)left)->ob_fval +
        #         ((PyFloatObject *)right)->ob_fval;
        #     sum = PyFloat_FromDouble(dsum);
        #     _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc);
        #     ERROR_IF(sum == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyFloat_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(cls.api.Py_TYPE(right) != cls.api.Py_TYPE(left), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        dsum = (left).ob_fval +
            (right).ob_fval
        sum = cls.api.PyFloat_FromDouble(dsum)
        cls.memory.dec_ref_specialized(right, cls.api.private.PyFloat_ExactDealloc)
        cls.memory.dec_ref_specialized(left, cls.api.private.PyFloat_ExactDealloc)
        cls.flow.error_if(sum == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, sum)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
