# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBuildConstKeyMap(OpCode):
    """
    The version of BUILD_MAP specialized for constant keys. Pops the
    top element on the stack which contains a tuple of keys, then starting from
    TOS1, pops count values to form values in the built dictionary.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_CONST_KEY_MAP
    """
    OPCODE_NAME = 'BUILD_CONST_KEY_MAP'
    OPCODE_VALUE = 156

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_CONST_KEY_MAP) {
        #     PyObject *map;
        #     PyObject *keys = TOP();
        #     if (!PyTuple_CheckExact(keys) ||
        #         PyTuple_GET_SIZE(keys) != (Py_ssize_t)oparg) {
        #         _PyErr_SetString(tstate, PyExc_SystemError,
        #                          "bad BUILD_CONST_KEY_MAP keys argument");
        #         goto error;
        #     }
        #     map = _PyDict_FromItems(
        #             &PyTuple_GET_ITEM(keys, 0), 1,
        #             &PEEK(oparg + 1), 1, oparg);
        #     if (map == NULL) {
        #         goto error;
        #     }

        #     Py_DECREF(POP());
        #     while (oparg--) {
        #         Py_DECREF(POP());
        #     }
        #     PUSH(map);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
