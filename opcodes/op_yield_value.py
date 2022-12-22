# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpYieldValue(OpCode):
    """
    Pops TOS and yields it from a generator.
    
    Changed in version 3.11: oparg set to be the stack depth, for efficient handling on frames.

    https://docs.python.org/3.12/library/dis.html#opcode-YIELD_VALUE
    """
    OPCODE_NAME = 'YIELD_VALUE'
    OPCODE_VALUE = 150

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(YIELD_VALUE) {
        #     // NOTE: It's important that YIELD_VALUE never raises an exception!
        #     // The compiler treats any exception raised here as a failed close()
        #     // or throw() call.
        #     assert(oparg == STACK_LEVEL());
        #     assert(frame != &entry_frame);
        #     PyObject *retval = POP();
        #     PyGenObject *gen = _PyFrame_GetGenerator(frame);
        #     gen->gi_frame_state = FRAME_SUSPENDED;
        #     _PyFrame_SetStackPointer(frame, stack_pointer);
        #     TRACE_FUNCTION_EXIT();
        #     DTRACE_FUNCTION_EXIT();
        #     tstate->exc_info = gen->gi_exc_state.previous_item;
        #     gen->gi_exc_state.previous_item = NULL;
        #     _Py_LeaveRecursiveCallPy(tstate);
        #     _PyInterpreterFrame *gen_frame = frame;
        #     frame = cframe.current_frame = frame->previous;
        #     gen_frame->previous = NULL;
        #     frame->prev_instr -= frame->yield_offset;
        #     _PyFrame_StackPush(frame, retval);
        #     goto resume_frame;
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
