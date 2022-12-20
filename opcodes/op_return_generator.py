# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpReturnGenerator(BaseOpCode):
    """
    Create a generator, coroutine, or async generator from the current frame.
    Clear the current frame and return the newly created generator.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-RETURN_GENERATOR
    """
    OPCODE_NAME = 'RETURN_GENERATOR'
    OPCODE_VALUE = 75

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(RETURN_GENERATOR) {
        #     assert(PyFunction_Check(frame->f_funcobj));
        #     PyFunctionObject *func = (PyFunctionObject *)frame->f_funcobj;
        #     PyGenObject *gen = (PyGenObject *)_Py_MakeCoro(func);
        #     if (gen == NULL) {
        #         goto error;
        #     }
        #     assert(EMPTY());
        #     _PyFrame_SetStackPointer(frame, stack_pointer);
        #     _PyInterpreterFrame *gen_frame = (_PyInterpreterFrame *)gen->gi_iframe;
        #     _PyFrame_Copy(frame, gen_frame);
        #     assert(frame->frame_obj == NULL);
        #     gen->gi_frame_state = FRAME_CREATED;
        #     gen_frame->owner = FRAME_OWNED_BY_GENERATOR;
        #     _Py_LeaveRecursiveCallPy(tstate);
        #     assert(frame != &entry_frame);
        #     _PyInterpreterFrame *prev = frame->previous;
        #     _PyThreadState_PopFrame(tstate, frame);
        #     frame = cframe.current_frame = prev;
        #     _PyFrame_StackPush(frame, (PyObject *)gen);
        #     goto resume_frame;
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
