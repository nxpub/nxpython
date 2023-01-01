# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinarySubscrDict(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_SUBSCR_DICT'
    value = 18

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_SUBSCR_DICT, (unused/4, dict, sub -- res)) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(dict), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     res = PyDict_GetItemWithError(dict, sub);
        #     if (res == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_SetKeyError(sub);
        #         }
        #         Py_DECREF(dict);
        #         Py_DECREF(sub);
        #         ERROR_IF(true, error);
        #     }
        #     Py_INCREF(res);  // Do this before DECREF'ing dict, sub
        #     DECREF_INPUTS();
        # }
        sub = cls.stack.peek(1)
        dict = cls.stack.peek(2)
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(not cls.api.PyDict_CheckExact(dict), 'BINARY_SUBSCR')
        cls.flow.stat_inc('BINARY_SUBSCR', 'hit')
        res = cls.api.PyDict_GetItemWithError(dict, sub)
        if res == None:
            if not cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.api.private.PyErr_SetKeyError(sub)
            cls.memory.dec_ref(dict)
            cls.memory.dec_ref(sub)
            cls.flow.error_if(True, 2)
        cls.memory.inc_ref(res)  # Do this before DECREF'ing dict, sub
        cls.memory.dec_ref(dict)
        cls.memory.dec_ref(sub)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.cache_offset(4)
        cls.flow.dispatch()
