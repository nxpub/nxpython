# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadConst(BaseOpCode):
    """
    Pushes co_consts[consti] onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CONST
    """
    OPCODE_NAME = 'LOAD_CONST'
    OPCODE_VALUE = 100

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_CONST) {
        #     PREDICTED(LOAD_CONST);
        #     PyObject *value;
        #     value = GETITEM(consts, oparg);
        #     Py_INCREF(value);
        #     STACK_GROW(1);
        #     POKE(1, value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
