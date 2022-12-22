# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpSetAdd(OpCode):
    """
    Calls set.add(TOS1[-i], TOS).  Used to implement set comprehensions.

    https://docs.python.org/3.12/library/dis.html#opcode-SET_ADD
    """
    OPCODE_NAME = 'SET_ADD'
    OPCODE_VALUE = 146

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, v) -> None:
        # TARGET(SET_ADD) {
        #     PyObject *v = PEEK(1);
        #     PyObject *set = PEEK(oparg + 1);  // +1 to account for v staying on stack
        #     int err = PySet_Add(set, v);
        #     Py_DECREF(v);
        #     if (err) goto pop_1_error;
        #     STACK_SHRINK(1);
        #     PREDICT(JUMP_BACKWARD);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
