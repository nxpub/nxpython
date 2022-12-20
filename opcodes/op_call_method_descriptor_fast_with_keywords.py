# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallMethodDescriptorFastWithKeywords(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS'
    OPCODE_VALUE = 34

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS) {
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyMethodDescrObject *callable =
        #         (PyMethodDescrObject *)PEEK(total_args + 1);
        #     DEOPT_IF(!Py_IS_TYPE(callable, &PyMethodDescr_Type), CALL);
        #     PyMethodDef *meth = callable->d_method;
        #     DEOPT_IF(meth->ml_flags != (METH_FASTCALL|METH_KEYWORDS), CALL);
        #     PyTypeObject *d_type = callable->d_common.d_type;
        #     PyObject *self = PEEK(total_args);
        #     DEOPT_IF(!Py_IS_TYPE(self, d_type), CALL);
        #     STAT_INC(CALL, hit);
        #     int nargs = total_args-1;
        #     STACK_SHRINK(nargs);
        #     _PyCFunctionFastWithKeywords cfunc =
        #         (_PyCFunctionFastWithKeywords)(void(*)(void))meth->ml_meth;
        #     PyObject *res = cfunc(self, stack_pointer, nargs - KWNAMES_LEN(),
        #                           kwnames);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     kwnames = NULL;

        #     /* Free the arguments. */
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
