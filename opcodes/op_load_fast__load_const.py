# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadFastLoadConst(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'LOAD_FAST__LOAD_CONST'
    OPCODE_VALUE = 121

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_FAST__LOAD_CONST) {
        #     PyObject *_tmp_1;
        #     PyObject *_tmp_2;
        #     {
        #         PyObject *value;
        #         value = GETLOCAL(oparg);
        #         assert(value != NULL);
        #         Py_INCREF(value);
        #         _tmp_2 = value;
        #     }
        #     NEXTOPARG();
        #     JUMPBY(1);
        #     {
        #         PyObject *value;
        #         value = GETITEM(consts, oparg);
        #         Py_INCREF(value);
        #         _tmp_1 = value;
        #     }
        #     STACK_GROW(2);
        #     POKE(1, _tmp_1);
        #     POKE(2, _tmp_2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
