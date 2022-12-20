# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallBuiltinFastWithKeywords(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_BUILTIN_FAST_WITH_KEYWORDS'
    OPCODE_VALUE = 29

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_BUILTIN_FAST_WITH_KEYWORDS) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_FASTCALL | METH_KEYWORDS functions */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) !=
        #         (METH_FASTCALL | METH_KEYWORDS), CALL);
        #     STAT_INC(CALL, hit);
        #     STACK_SHRINK(total_args);
        #     /* res = func(self, args, nargs, kwnames) */
        #     _PyCFunctionFastWithKeywords cfunc =
        #         (_PyCFunctionFastWithKeywords)(void(*)(void))
        #         PyCFunction_GET_FUNCTION(callable);
        #     PyObject *res = cfunc(
        #         PyCFunction_GET_SELF(callable),
        #         stack_pointer,
        #         total_args - KWNAMES_LEN(),
        #         kwnames
        #     );
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     kwnames = NULL;

        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     PUSH(res);
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
