# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallBuiltinClass(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_BUILTIN_CLASS'
    OPCODE_VALUE = 28

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_BUILTIN_CLASS) {
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     int kwnames_len = KWNAMES_LEN();
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyType_Check(callable), CALL);
        #     PyTypeObject *tp = (PyTypeObject *)callable;
        #     DEOPT_IF(tp->tp_vectorcall == NULL, CALL);
        #     STAT_INC(CALL, hit);
        #     STACK_SHRINK(total_args);
        #     PyObject *res = tp->tp_vectorcall((PyObject *)tp, stack_pointer,
        #                                       total_args-kwnames_len, kwnames);
        #     kwnames = NULL;
        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     Py_DECREF(tp);
        #     STACK_SHRINK(1-is_meth);
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
