# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwStr1(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_STR_1'
    OPCODE_VALUE = 46

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_STR_1) {
        #     assert(kwnames == NULL);
        #     assert(cframe.use_tracing == 0);
        #     assert(oparg == 1);
        #     DEOPT_IF(is_method(stack_pointer, 1), CALL);
        #     PyObject *callable = PEEK(2);
        #     DEOPT_IF(callable != (PyObject *)&PyUnicode_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = TOP();
        #     PyObject *res = PyObject_Str(arg);
        #     Py_DECREF(arg);
        #     Py_DECREF(&PyUnicode_Type);
        #     STACK_SHRINK(2);
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
