# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpDictUpdate(OpCode):
    """
    Calls dict.update(TOS1[-i], TOS).  Used to build dicts.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-DICT_UPDATE
    """
    OPCODE_NAME = 'DICT_UPDATE'
    OPCODE_VALUE = 165

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DICT_UPDATE) {
        #     PyObject *update = POP();
        #     PyObject *dict = PEEK(oparg);
        #     if (PyDict_Update(dict, update) < 0) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_AttributeError)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                             "'%.200s' object is not a mapping",
        #                             Py_TYPE(update)->tp_name);
        #         }
        #         Py_DECREF(update);
        #         goto error;
        #     }
        #     Py_DECREF(update);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
