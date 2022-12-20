# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpListAppend(BaseOpCode):
    """
    Calls list.append(TOS1[-i], TOS).  Used to implement list comprehensions.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_APPEND
    """
    OPCODE_NAME = 'LIST_APPEND'
    OPCODE_VALUE = 145

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, v) -> None:
        # TARGET(LIST_APPEND) {
        #     PyObject *v = PEEK(1);
        #     PyObject *list = PEEK(oparg + 1);  // +1 to account for v staying on stack
        #     if (_PyList_AppendTakeRef((PyListObject *)list, v) < 0) goto pop_1_error;
        #     STACK_SHRINK(1);
        #     PREDICT(JUMP_BACKWARD);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
