# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwMethodDescriptorFast(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_METHOD_DESCRIPTOR_FAST'
    OPCODE_VALUE = 43

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_METHOD_DESCRIPTOR_FAST) {
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyMethodDescrObject *callable =
        #         (PyMethodDescrObject *)PEEK(total_args + 1);
        #     /* Builtin METH_FASTCALL methods, without keywords */
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     DEOPT_IF(meth->ml_flags != METH_FASTCALL, CALL);
        #     PyObject *self = PEEK(total_args);
        #     DEOPT_IF(!Py_IS_TYPE(self, callable->d_common.d_type), CALL);
        #     STAT_INC(CALL, hit);
        #     _PyCFunctionFast cfunc =
        #         (_PyCFunctionFast)(void(*)(void))meth->ml_meth;
        #     int nargs = total_args-1;
        #     STACK_SHRINK(nargs);
        #     PyObject *res = cfunc(self, stack_pointer, nargs);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     /* Clear the stack of the arguments. */
        #     for (int i = 0; i < nargs; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     Py_DECREF(self);
        #     STACK_SHRINK(2-is_meth);
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
