# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinaryOpAddInt(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_OP_ADD_INT'
    value = 6

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_OP_ADD_INT, (unused/1, left, right -- sum)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyLong_CheckExact(left), BINARY_OP);
        #     DEOPT_IF(Py_TYPE(right) != Py_TYPE(left), BINARY_OP);
        #     STAT_INC(BINARY_OP, hit);
        #     sum = _PyLong_Add((PyLongObject *)left, (PyLongObject *)right);
        #     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #     ERROR_IF(sum == NULL, error);
        # }
        right = cls.stack.peek(1)
        left = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyLong_CheckExact(left), 'BINARY_OP')
        cls.flow.deopt_if(cls.api.Py_TYPE(right) != cls.api.Py_TYPE(left), 'BINARY_OP')
        cls.flow.stat_inc('BINARY_OP', 'hit')
        sum = cls.api.private.PyLong_Add(left, right)
        cls.memory.dec_ref_specialized(right, cls.api.PyObject_Free)
        cls.memory.dec_ref_specialized(left, cls.api.PyObject_Free)
        cls.flow.error_if(sum == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, sum)
        cls.flow.cache_offset(1)
        cls.flow.dispatch()
