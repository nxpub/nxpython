# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpForIterGen(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'FOR_ITER_GEN'
    value = 65

    @classmethod
    def logic(cls) -> None:
        # inst(FOR_ITER_GEN) {
        #     assert(cframe.use_tracing == 0);
        #     PyGenObject *gen = (PyGenObject *)TOP();
        #     DEOPT_IF(Py_TYPE(gen) != &PyGen_Type, FOR_ITER);
        #     DEOPT_IF(gen->gi_frame_state >= FRAME_EXECUTING, FOR_ITER);
        #     STAT_INC(FOR_ITER, hit);
        #     _PyInterpreterFrame *gen_frame = (_PyInterpreterFrame *)gen->gi_iframe;
        #     frame->yield_offset = oparg;
        #     _PyFrame_StackPush(gen_frame, Py_NewRef(Py_None));
        #     gen->gi_frame_state = FRAME_EXECUTING;
        #     gen->gi_exc_state.previous_item = tstate->exc_info;
        #     tstate->exc_info = &gen->gi_exc_state;
        #     JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg);
        #     assert(_Py_OPCODE(*next_instr) == END_FOR);
        #     DISPATCH_INLINED(gen_frame);
        # }
        # assert(cframe.use_tracing == 0)
        gen = cls.stack.top()
        cls.flow.deopt_if(cls.api.Py_TYPE(gen) != cls.api.PyGen_Type, 'FOR_ITER')
        cls.flow.deopt_if(gen.gi_frame_state >= FRAME_EXECUTING, 'FOR_ITER')
        cls.flow.stat_inc('FOR_ITER', 'hit')
        gen_frame = gen.gi_iframe
        frame.yield_offset = oparg
        cls.api.private.PyFrame_StackPush(gen_frame, cls.api.Py_NewRef(cls.api.Py_None))
        gen.gi_frame_state = FRAME_EXECUTING
        gen.gi_exc_state.previous_item = cls.frame.state.exc_info
        cls.frame.state.exc_info = gen.gi_exc_state
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER + oparg)
        # assert(_Py_OPCODE(*next_instr) == END_FOR)
        DISPATCH_INLINED(gen_frame)
