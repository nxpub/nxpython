# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpDeleteFast(BaseOpCode):
    """
    Deletes local co_varnames[var_num].

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_FAST
    """
    OPCODE_NAME = 'DELETE_FAST'
    OPCODE_VALUE = 126

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DELETE_FAST) {
        #     PyObject *v = GETLOCAL(oparg);
        #     if (v == NULL) goto unbound_local_error;
        #     SETLOCAL(oparg, NULL);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
