# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpGetIter(OpCode):
    """
    Implements TOS = iter(TOS).

    https://docs.python.org/3.12/library/dis.html#opcode-GET_ITER
    """
    OPCODE_NAME = 'GET_ITER'
    OPCODE_VALUE = 68

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(GET_ITER) {
        #     /* before: [obj]; after [getiter(obj)] */
        #     PyObject *iterable = TOP();
        #     PyObject *iter = PyObject_GetIter(iterable);
        #     Py_DECREF(iterable);
        #     SET_TOP(iter);
        #     if (iter == NULL)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
