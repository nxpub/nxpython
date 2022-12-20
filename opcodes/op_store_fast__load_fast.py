# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreFastLoadFast(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_FAST__LOAD_FAST'
    OPCODE_VALUE = 160

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(STORE_FAST__LOAD_FAST) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     {
        #         PyObject *value = _tmp_1;
        #         SETLOCAL(oparg, value);
        #     }
        #     NEXTOPARG();
        #     JUMPBY(1);
        #     {
        #         PyObject *value;
        #         value = GETLOCAL(oparg);
        #         assert(value != NULL);
        #         Py_INCREF(value);
        #         _tmp_1 = value;
        #     }
        #     POKE(1, _tmp_1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
