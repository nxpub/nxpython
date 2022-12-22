# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpInterpreterExit(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'INTERPRETER_EXIT'
    OPCODE_VALUE = 3

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, retval) -> None:
        # TARGET(INTERPRETER_EXIT) {
        #     PyObject *retval = PEEK(1);
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
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
