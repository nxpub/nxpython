# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCallNoKwType1(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_NO_KW_TYPE_1'
    OPCODE_VALUE = 48

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_NO_KW_TYPE_1) {
        #     assert(kwnames == NULL);
        #     assert(cframe.use_tracing == 0);
        #     assert(oparg == 1);
        #     DEOPT_IF(is_method(stack_pointer, 1), CALL);
        #     PyObject *obj = TOP();
        #     PyObject *callable = SECOND();
        #     DEOPT_IF(callable != (PyObject *)&PyType_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     PyObject *res = Py_NewRef(Py_TYPE(obj));
        #     Py_DECREF(callable);
        #     Py_DECREF(obj);
        #     STACK_SHRINK(2);
        #     SET_TOP(res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
