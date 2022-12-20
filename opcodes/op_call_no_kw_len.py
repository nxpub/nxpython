# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwLen(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_LEN'
    OPCODE_VALUE = 41

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_LEN) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     /* len(o) */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     DEOPT_IF(total_args != 1, CALL);
        #     PyObject *callable = PEEK(total_args + 1);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.len, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = TOP();
        #     Py_ssize_t len_i = PyObject_Length(arg);
        #     if (len_i < 0) {
        #         goto error;
        #     }
        #     PyObject *res = PyLong_FromSsize_t(len_i);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     Py_DECREF(callable);
        #     Py_DECREF(arg);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
