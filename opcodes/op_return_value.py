# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpReturnValue(BaseOpCode):
    """
    Returns with TOS to the caller of the function.

    https://docs.python.org/3.12/library/dis.html#opcode-RETURN_VALUE
    """
    OPCODE_NAME = 'RETURN_VALUE'
    OPCODE_VALUE = 83

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, retval) -> None:
        # TARGET(RETURN_VALUE) {
        #     PyObject *retval = PEEK(1);
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
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
