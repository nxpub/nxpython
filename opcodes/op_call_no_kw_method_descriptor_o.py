# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallNoKwMethodDescriptorO(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_METHOD_DESCRIPTOR_O'
    OPCODE_VALUE = 45

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_METHOD_DESCRIPTOR_O) {
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyMethodDescrObject *callable =
        #         (PyMethodDescrObject *)PEEK(total_args + 1);
        #     DEOPT_IF(total_args != 2, CALL);
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     DEOPT_IF(meth->ml_flags != METH_O, CALL);
        #     PyObject *arg = TOP();
        #     PyObject *self = SECOND();
        #     DEOPT_IF(!Py_IS_TYPE(self, callable->d_common.d_type), CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = meth->ml_meth;
        #     // This is slower but CPython promises to check all non-vectorcall
        #     // function calls.
        #     if (_Py_EnterRecursiveCallTstate(tstate, " while calling a Python object")) {
        #         goto error;
        #     }
        #     PyObject *res = _PyCFunction_TrampolineCall(cfunc, self, arg);
        #     _Py_LeaveRecursiveCallTstate(tstate);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     Py_DECREF(self);
        #     Py_DECREF(arg);
        #     STACK_SHRINK(oparg + 1);
        #     SET_TOP(res);
        #     Py_DECREF(callable);
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
