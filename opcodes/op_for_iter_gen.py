# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpForIterGen(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'FOR_ITER_GEN'
    OPCODE_VALUE = 65

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(FOR_ITER_GEN) {
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
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
