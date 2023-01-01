# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBinarySubscrGetitem(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'BINARY_SUBSCR_GETITEM'
    value = 19

    @classmethod
    def logic(cls) -> None:
        # inst(BINARY_SUBSCR_GETITEM, (unused/1, type_version/2, func_version/1, container, sub -- unused)) {
        #     PyTypeObject *tp = Py_TYPE(container);
        #     DEOPT_IF(tp->tp_version_tag != type_version, BINARY_SUBSCR);
        #     assert(tp->tp_flags & Py_TPFLAGS_HEAPTYPE);
        #     PyObject *cached = ((PyHeapTypeObject *)tp)->_spec_cache.getitem;
        #     assert(PyFunction_Check(cached));
        #     PyFunctionObject *getitem = (PyFunctionObject *)cached;
        #     DEOPT_IF(getitem->func_version != func_version, BINARY_SUBSCR);
        #     PyCodeObject *code = (PyCodeObject *)getitem->func_code;
        #     assert(code->co_argcount == 2);
        #     DEOPT_IF(!_PyThreadState_HasStackSpace(tstate, code->co_framesize), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     Py_INCREF(getitem);
        #     _PyInterpreterFrame *new_frame = _PyFrame_PushUnchecked(tstate, getitem);
        #     STACK_SHRINK(2);
        #     new_frame->localsplus[0] = container;
        #     new_frame->localsplus[1] = sub;
        #     for (int i = 2; i < code->co_nlocalsplus; i++) {
        #         new_frame->localsplus[i] = NULL;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_BINARY_SUBSCR);
        #     DISPATCH_INLINED(new_frame);
        # }
        sub = cls.stack.peek(1)
        container = cls.stack.peek(2)
        type_version = read_u32(next_instr[1].cache)
        func_version = read_u16(next_instr[3].cache)
        tp = cls.api.Py_TYPE(container)
        cls.flow.deopt_if(tp.tp_version_tag != type_version, 'BINARY_SUBSCR')
        # assert(tp->tp_flags & Py_TPFLAGS_HEAPTYPE)
        cached = (tp)._spec_cache.getitem
        # assert(PyFunction_Check(cached))
        getitem = cached
        cls.flow.deopt_if(getitem.func_version != func_version, 'BINARY_SUBSCR')
        code = getitem.func_code
        # assert(code->co_argcount == 2)
        cls.flow.deopt_if(not cls.api.private.PyThreadState_HasStackSpace(cls.frame.state, 'code.co_framesize'), BINARY_SUBSCR)
        cls.flow.stat_inc('BINARY_SUBSCR', 'hit')
        cls.memory.inc_ref(getitem)
        new_frame = cls.api.private.PyFrame_PushUnchecked(cls.frame.state, getitem)
        cls.stack.shrink(2)
        new_frame.localsplus[0] = container
        new_frame.localsplus[1] = sub
        for (int i = 2 i < code.co_nlocalsplus i++) {
            new_frame.localsplus[i] = None
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_BINARY_SUBSCR)
        DISPATCH_INLINED(new_frame)
