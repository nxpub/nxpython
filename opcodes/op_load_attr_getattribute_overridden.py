# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttrGetattributeOverridden(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN'
    value = 67

    @classmethod
    def logic(cls) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN) {
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(tstate->interp->eval_frame, LOAD_ATTR);
        #     _PyLoadMethodCache *cache = (_PyLoadMethodCache *)next_instr;
        #     PyObject *owner = TOP();
        #     PyTypeObject *cls = Py_TYPE(owner);
        #     uint32_t type_version = read_u32(cache->type_version);
        #     DEOPT_IF(cls->tp_version_tag != type_version, LOAD_ATTR);
        #     assert(type_version != 0);
        #     PyObject *getattribute = read_obj(cache->descr);
        #     assert(Py_IS_TYPE(getattribute, &PyFunction_Type));
        #     PyFunctionObject *f = (PyFunctionObject *)getattribute;
        #     uint32_t func_version = read_u32(cache->keys_version);
        #     assert(func_version != 0);
        #     DEOPT_IF(f->func_version != func_version, LOAD_ATTR);
        #     PyCodeObject *code = (PyCodeObject *)f->func_code;
        #     assert(code->co_argcount == 2);
        #     DEOPT_IF(!_PyThreadState_HasStackSpace(tstate, code->co_framesize), LOAD_ATTR);
        #     STAT_INC(LOAD_ATTR, hit);

        #     PyObject *name = GETITEM(names, oparg >> 1);
        #     Py_INCREF(f);
        #     _PyInterpreterFrame *new_frame = _PyFrame_PushUnchecked(tstate, f);
        #     SET_TOP(NULL);
        #     int shrink_stack = !(oparg & 1);
        #     STACK_SHRINK(shrink_stack);
        #     new_frame->localsplus[0] = owner;
        #     new_frame->localsplus[1] = Py_NewRef(name);
        #     for (int i = 2; i < code->co_nlocalsplus; i++) {
        #         new_frame->localsplus[i] = NULL;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        #     DISPATCH_INLINED(new_frame);
        # }
        # assert(cframe.use_tracing == 0)
        cls.flow.deopt_if(cls.frame.state.interp.eval_frame, 'LOAD_ATTR')

