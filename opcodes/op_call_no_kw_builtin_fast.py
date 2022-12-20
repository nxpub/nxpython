# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwBuiltinFast(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_BUILTIN_FAST'
    OPCODE_VALUE = 38

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_BUILTIN_FAST) {
        #     assert(cframe.use_tracing == 0);
        #     /* Builtin METH_FASTCALL functions, without keywords */
        #     assert(kwnames == NULL);
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(!PyCFunction_CheckExact(callable), CALL);
        #     DEOPT_IF(PyCFunction_GET_FLAGS(callable) != METH_FASTCALL,
        #         CALL);
        #     STAT_INC(CALL, hit);
        #     PyCFunction cfunc = PyCFunction_GET_FUNCTION(callable);
        #     STACK_SHRINK(total_args);
        #     /* res = func(self, args, nargs) */
        #     PyObject *res = ((_PyCFunctionFast)(void(*)(void))cfunc)(
        #         PyCFunction_GET_SELF(callable),
        #         stack_pointer,
        #         total_args);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     /* Free the arguments. */
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     PUSH(res);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         /* Not deopting because this doesn't mean our optimization was
        #            wrong. `res` can be NULL for valid reasons. Eg. getattr(x,
        #            'invalid'). In those cases an exception is set, so we must
        #            handle it.
        #         */
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
