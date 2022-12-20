# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBinarySubscrDict(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'BINARY_SUBSCR_DICT'
    OPCODE_VALUE = 18

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, dict, sub) -> None:
        # TARGET(BINARY_SUBSCR_DICT) {
        #     PyObject *sub = PEEK(1);
        #     PyObject *dict = PEEK(2);
        #     PyObject *res;
        #     assert(cframe.use_tracing == 0);
        #     DEOPT_IF(!PyDict_CheckExact(dict), BINARY_SUBSCR);
        #     STAT_INC(BINARY_SUBSCR, hit);
        #     res = PyDict_GetItemWithError(dict, sub);
        #     if (res == NULL) {
        #         if (!_PyErr_Occurred(tstate)) {
        #             _PyErr_SetKeyError(sub);
        #         }
        #         Py_DECREF(dict);
        #         Py_DECREF(sub);
        #         if (true) goto pop_2_error;
        #     }
        #     Py_INCREF(res);  // Do this before DECREF'ing dict, sub
        #     Py_DECREF(dict);
        #     Py_DECREF(sub);
        #     STACK_SHRINK(1);
        #     POKE(1, res);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
