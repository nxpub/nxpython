# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallNoKwBuiltinO(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_BUILTIN_O'
    OPCODE_VALUE = 39

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_BUILTIN_O) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_O functions */
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     DEOPT_IF(total_args != 1, CALL);
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_O, CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = PyCFunction_GET_FUNCTION(callable);
        #     // This is slower but CPython promises to check all non-vectorcall
        #     // function calls.
        #     if (_Py_EnterRecursiveCallTstate(tstate, " while calling a Python object")) {
        #         goto error;
        #     }
        #     PyObject *arg = TOP();
        #     PyObject *res = _PyCFunction_TrampolineCall(cfunc, PyCFunction_GET_SELF(callable), arg);
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     Py_DECREF(arg);
        #     Py_DECREF(callable);
        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
