# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwStr1(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_STR_1'
    value = 46

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_STR_1) {
        #     assert(kwnames == NULL);
        #     assert(cframe.use_tracing == 0);
        #     assert(oparg == 1);
        #     DEOPT_IF(is_method(stack_pointer, 1), CALL);
        #     PyObject *callable = PEEK(2);
        #     DEOPT_IF(callable != (PyObject *)&PyUnicode_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = TOP();
        #     PyObject *res = PyObject_Str(arg);
        #     Py_DECREF(arg);
        #     Py_DECREF(&PyUnicode_Type);
        #     STACK_SHRINK(2);
        #     SET_TOP(res);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        # }
        # assert(kwnames == NULL)
        # assert(cframe.use_tracing == 0)
        # assert(oparg == 1)
        cls.flow.deopt_if(is_method(cls.stack, '1'), CALL)
        callable = cls.stack.peek(2)
        cls.flow.deopt_if(callable != cls.api.PyUnicode_Type, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        arg = cls.stack.top()
        res = cls.api.PyObject_Str(arg)
        cls.memory.dec_ref(arg)
        cls.memory.dec_ref(cls.api.PyUnicode_Type)
        cls.stack.shrink(2)
        cls.stack.set_top(res)
        if res == None:
            cls.flow.error()
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL)
        cls.flow.check_eval_breaker()
        cls.flow.dispatch()
