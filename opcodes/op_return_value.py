# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpReturnValue(OpCode):
    """
    Returns with TOS to the caller of the function.

    https://docs.python.org/3.12/library/dis.html#opcode-RETURN_VALUE
    """
    name = 'RETURN_VALUE'
    value = 83

    @classmethod
    def logic(cls) -> None:
        # inst(RETURN_VALUE, (retval --)) {
        #     STACK_SHRINK(1);
        #     assert(EMPTY());
        #     _PyFrame_SetStackPointer(frame, stack_pointer);
        #     TRACE_FUNCTION_EXIT();
        #     DTRACE_FUNCTION_EXIT();
        #     _Py_LeaveRecursiveCallPy(tstate);
        #     assert(frame != &entry_frame);
        #     // GH-99729: We need to unlink the frame *before* clearing it:
        #     _PyInterpreterFrame *dying = frame;
        #     frame = cframe.current_frame = dying->previous;
        #     _PyEvalFrameClearAndPop(tstate, dying);
        #     _PyFrame_StackPush(frame, retval);
        #     goto resume_frame;
        # }
        retval = cls.stack.peek(1)
        cls.stack.shrink(1)
        # assert(EMPTY())
        cls.api.private.PyFrame_SetStackPointer(frame, cls.stack)
        TRACE_FUNCTION_EXIT()
        DTRACE_FUNCTION_EXIT()
        cls.api.private.Py_LeaveRecursiveCallPy(cls.frame.state)
        # assert(frame != &entry_frame)
        # GH-99729: We need to unlink the frame *before* clearing it:
        dying = frame
        frame = cframe.current_frame = dying.previous
        cls.api.private.PyEvalFrameClearAndPop(cls.frame.state, dying)
        cls.api.private.PyFrame_StackPush(frame, retval)
        cls.flow.resume_frame()
