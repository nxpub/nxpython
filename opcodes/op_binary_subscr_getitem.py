# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBinarySubscrGetitem(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_SUBSCR_GETITEM'
    OPCODE_VALUE = 19

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, type_version, func_version, container, sub) -> None:
        # TARGET(BINARY_SUBSCR_GETITEM) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *container = PEEK(2);
        #     uint32_t type_version = read_u32(&next_instr[1].cache);
        #     uint16_t func_version = read_u16(&next_instr[3].cache);
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
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
