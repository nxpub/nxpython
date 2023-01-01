# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpAddUnicode(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_ADD_UNICODE'
    value = 7

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_ADD_UNICODE, (unused/1, left, right -- res)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyUnicode_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     res = PyUnicode_Concat(left, right);
        #     _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc);
        #     _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc);
        #     ERROR_IF(res == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyUnicode_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(cls.api.Py_TYPE(right) != cls.api.Py_TYPE(left), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        res = cls.api.PyUnicode_Concat(left, right)
        cls.memory.dec_ref_specialized(left, cls.api.private.PyUnicode_ExactDealloc)
        cls.memory.dec_ref_specialized(right, cls.api.private.PyUnicode_ExactDealloc)
        cls.flow.error_if(res == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
