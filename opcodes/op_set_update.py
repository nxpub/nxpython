# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpSetUpdate(BaseOpCode):
    """
    Calls set.update(TOS1[-i], TOS).  Used to build sets.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-SET_UPDATE
    """
    OPCODE_NAME = 'SET_UPDATE'
    OPCODE_VALUE = 163

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(SET_UPDATE) {
        #     PyObject *iterable = POP();
        #     PyObject *set = PEEK(oparg);
        #     int err = _PySet_Update(set, iterable);
        #     Py_DECREF(iterable);
        #     if (err < 0) {
        #         goto error;
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
