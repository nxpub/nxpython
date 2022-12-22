# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallNoKwTuple1(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_TUPLE_1'
    OPCODE_VALUE = 47

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_TUPLE_1) {
        #     assert(kwnames == NULL);
        #     assert(oparg == 1);
        #     DEOPT_IF(is_method(stack_pointer, 1), CALL);
        #     PyObject *callable = PEEK(2);
        #     DEOPT_IF(callable != (PyObject *)&PyTuple_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *arg = TOP();
        #     PyObject *res = PySequence_Tuple(arg);
        #     Py_DECREF(arg);
        #     Py_DECREF(&PyTuple_Type);
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
