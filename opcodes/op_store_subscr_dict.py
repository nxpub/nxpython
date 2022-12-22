# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreSubscrDict(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_SUBSCR_DICT'
    OPCODE_VALUE = 166

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, value, dict, sub) -> None:
        # TARGET(STORE_SUBSCR_DICT) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *dict = PEEK(2);
        #     PyObject *value = PEEK(3);
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(dict), STORE_SUBSCR);
        #     STAT_INC(STORE_SUBSCR, hit);
        #     int err = _PyDict_SetItem_Take2((PyDictObject *)dict, sub, value);
        #     Py_DECREF(dict);
        #     if (err) goto pop_3_error;
        #     STACK_SHRINK(3);
        #     JUMPBY(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
