# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpStoreFast(OpCode):
    """
    Stores TOS into the local co_varnames[var_num].

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_FAST
    """
    OPCODE_NAME = 'STORE_FAST'
    OPCODE_VALUE = 125

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(STORE_FAST) {
        #     PyObject *value = PEEK(1);
        #     SETLOCAL(oparg, value);
        #     STACK_SHRINK(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
