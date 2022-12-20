# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreFastStoreFast(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_FAST__STORE_FAST'
    OPCODE_VALUE = 161

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(STORE_FAST__STORE_FAST) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     PyObject *_tmp_2 = PEEK(2);
        #     {
        #         PyObject *value = _tmp_1;
        #         SETLOCAL(oparg, value);
        #     }
        #     NEXTOPARG();
        #     JUMPBY(1);
        #     {
        #         PyObject *value = _tmp_2;
        #         SETLOCAL(oparg, value);
        #     }
        #     STACK_SHRINK(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
