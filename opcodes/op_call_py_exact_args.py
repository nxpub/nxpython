# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallPyExactArgs(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_PY_EXACT_ARGS'
    value = 22

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_PY_EXACT_ARGS) {
        #     assert(kwnames == NULL);
        #     DEOPT_IF(tstate->interp->eval_frame, CALL);
        #     _PyCallCache *cache = (_PyCallCache *)next_instr;
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int argcount = oparg + is_meth;
        #     PyObject *callable = PEEK(argcount + 1);
        #     DEOPT_IF(!PyFunction_Check(callable), CALL);
        #     PyFunctionObject *func = (PyFunctionObject *)callable;
        #     DEOPT_IF(func->func_version != read_u32(cache->func_version), CALL);
        #     PyCodeObject *code = (PyCodeObject *)func->func_code;
        #     DEOPT_IF(code->co_argcount != argcount, CALL);
        #     DEOPT_IF(!_PyThreadState_HasStackSpace(tstate, code->co_framesize), CALL);
        #     STAT_INC(CALL, hit);
        #     _PyInterpreterFrame *new_frame = _PyFrame_PushUnchecked(tstate, func);
        #     STACK_SHRINK(argcount);
        #     for (int i = 0; i < argcount; i++) {
        #         new_frame->localsplus[i] = stack_pointer[i];
        #     }
        #     for (int i = argcount; i < code->co_nlocalsplus; i++) {
        #         new_frame->localsplus[i] = NULL;
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     DISPATCH_INLINED(new_frame);
        # }
        # assert(kwnames == NULL)
        cls.flow.deopt_if(cls.frame.state.interp.eval_frame, 'CALL')
