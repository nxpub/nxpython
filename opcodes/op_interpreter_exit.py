# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpInterpreterExit(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'INTERPRETER_EXIT'
    value = 3

    @classmethod
    def logic(cls) -> None:
        # inst(INTERPRETER_EXIT, (retval --)) {
        #     assert(frame == &entry_frame);
        #     assert(_PyFrame_IsIncomplete(frame));
        #     STACK_SHRINK(1);  // Since we're not going to DISPATCH()
        #     assert(EMPTY());
        #     /* Restore previous cframe and return. */
        #     tstate->cframe = cframe.previous;
        #     tstate->cframe->use_tracing = cframe.use_tracing;
        #     assert(tstate->cframe->current_frame == frame->previous);
        #     assert(!_PyErr_Occurred(tstate));
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     return retval;
        # }
        retval = cls.stack.peek(1)
        # assert(frame == &entry_frame)
        # assert(_PyFrame_IsIncomplete(frame))
        cls.stack.shrink(1)  # Since we're not going to DISPATCH()
        # assert(EMPTY())
        # Restore previous cframe and return. 
        cls.frame.state.cframe = cframe.previous
        cls.frame.state.cframe.use_tracing = cframe.use_tracing
        # assert(tstate->cframe->current_frame == frame->previous)
        # assert(!_PyErr_Occurred(tstate))
        cls.api.private.Py_LeaveRecursiveCallTstate(cls.frame.state)
