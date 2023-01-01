# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwType1(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_TYPE_1'
    value = 48

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_TYPE_1) {
        #     assert(kwnames == NULL);
        #     assert(cframe.use_tracing == 0);
        #     assert(oparg == 1);
        #     DEOPT_IF(is_method(stack_pointer, 1), CALL);
        #     PyObject *obj = TOP();
        #     PyObject *callable = SECOND();
        #     DEOPT_IF(callable != (PyObject *)&PyType_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     PyObject *res = Py_NewRef(Py_TYPE(obj));
        #     Py_DECREF(callable);
        #     Py_DECREF(obj);
        #     STACK_SHRINK(2);
        #     SET_TOP(res);
        # }
        # assert(kwnames == NULL)
        # assert(cframe.use_tracing == 0)
        # assert(oparg == 1)
        cls.flow.deopt_if(is_method(cls.stack, '1'), CALL)
        obj = cls.stack.top()
        callable = cls.stack.second()
        cls.flow.deopt_if(callable != cls.api.PyType_Type, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        res = cls.api.Py_NewRef(cls.api.Py_TYPE(obj))
        cls.memory.dec_ref(callable)
        cls.memory.dec_ref(obj)
        cls.stack.shrink(2)
        cls.stack.set_top(res)
        cls.flow.dispatch()
