# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpReturnGenerator(OpCode):
    """
    Create a generator, coroutine, or async generator from the current frame.
    Clear the current frame and return the newly created generator.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-RETURN_GENERATOR
    """
    name = 'RETURN_GENERATOR'
    value = 75

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- )
        # inst(RETURN_GENERATOR) {
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
        # assert(PyFunction_Check(frame->f_funcobj))
        func = frame.f_funcobj
        gen = cls.api.private.Py_MakeCoro(func)
        if gen == None:
            cls.flow.error()
        # assert(EMPTY())
        cls.api.private.PyFrame_SetStackPointer(frame, cls.stack)
        gen_frame = gen.gi_iframe
        cls.api.private.PyFrame_Copy(frame, gen_frame)
        # assert(frame->frame_obj == NULL)
        gen.gi_frame_state = FRAME_CREATED
        gen_frame.owner = FRAME_OWNED_BY_GENERATOR
        cls.api.private.Py_LeaveRecursiveCallPy(cls.frame.state)
        # assert(frame != &entry_frame)
        prev = frame.previous
        cls.api.private.PyThreadState_PopFrame(cls.frame.state, frame)
        frame = cframe.current_frame = prev
        cls.api.private.PyFrame_StackPush(frame, gen)
        cls.flow.resume_frame()
