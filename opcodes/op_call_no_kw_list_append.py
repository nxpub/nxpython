# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallNoKwListAppend(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_NO_KW_LIST_APPEND'
    value = 42

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_NO_KW_LIST_APPEND) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     assert(oparg == 1);
        #     PyObject *callable = PEEK(3);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.list_append, CALL);
        #     PyObject *list = SECOND();
        #     DEOPT_IF(!PyList_Check(list), CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = POP();
        #     if (_PyList_AppendTakeRef((PyListObject *)list, arg) < 0) {
        #         goto error;
        #     }
        #     STACK_SHRINK(2);
        #     Py_DECREF(list);
        #     Py_DECREF(callable);
        #     // CALL + POP_TOP
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL + 1);
        #     assert(_Py_OPCODE(next_instr[-1]) == POP_TOP);
        # }
        # assert(cframe.use_tracing == 0)
        # assert(kwnames == NULL)
        # assert(oparg == 1)
        callable = cls.stack.peek(3)
        interp = cls.api.private.PyInterpreterState_GET()
        cls.flow.deopt_if(callable != interp.callable_cache.list_append, 'CALL')
        list = cls.stack.second()
        cls.flow.deopt_if(not cls.api.PyList_Check(list), 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        arg = cls.stack.pop()
        if cls.api.private.PyList_AppendTakeRef(list, arg) < 0:
            cls.flow.error()
        cls.stack.shrink(2)
        cls.memory.dec_ref(list)
        cls.memory.dec_ref(callable)
        # CALL + POP_TOP
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_CALL + 1)
        # assert(_Py_OPCODE(next_instr[-1]) == POP_TOP)
        cls.flow.dispatch()
