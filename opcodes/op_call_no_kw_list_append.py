# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwListAppend(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_LIST_APPEND'
    OPCODE_VALUE = 42

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_LIST_APPEND) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     assert(oparg == 1);
        #     PyObject *callable = PEEK(3);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.list_append, CALL);
        #     PyObject *list = SECOND();
        #     DEOPT_IF(!PyList_Check(list), CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = POP();
        #     if (_PyList_AppendTakeRef((PyListObject *)list, arg) < 0) {
        #         goto error;
        #     }
        #     STACK_SHRINK(2);
        #     Py_DECREF(list);
        #     Py_DECREF(callable);
        #     // CALL + POP_TOP
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL + 1);
        #     assert(_Py_OPCODE(next_instr[-1]) == POP_TOP);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
