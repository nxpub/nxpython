# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallNoKwIsinstance(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_ISINSTANCE'
    OPCODE_VALUE = 40

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_ISINSTANCE) {
        #     assert(cframe.use_tracing == 0);
        #     assert(kwnames == NULL);
        #     /* isinstance(o, o2) */
        #     int is_meth = is_method(stack_pointer, oparg);
        #     int total_args = oparg + is_meth;
        #     PyObject *callable = PEEK(total_args + 1);
        #     DEOPT_IF(total_args != 2, CALL);
        #     PyInterpreterState *interp = _PyInterpreterState_GET();
        #     DEOPT_IF(callable != interp->callable_cache.isinstance, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *cls = POP();
        #     PyObject *inst = TOP();
        #     int retval = PyObject_IsInstance(inst, cls);
        #     if (retval < 0) {
        #         Py_DECREF(cls);
        #         goto error;
        #     }
        #     PyObject *res = PyBool_FromLong(retval);
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));

        #     STACK_SHRINK(2-is_meth);
        #     SET_TOP(res);
        #     Py_DECREF(inst);
        #     Py_DECREF(cls);
        #     Py_DECREF(callable);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
