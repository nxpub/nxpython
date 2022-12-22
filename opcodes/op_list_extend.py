# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpListExtend(OpCode):
    """
    Calls list.extend(TOS1[-i], TOS).  Used to build lists.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_EXTEND
    """
    OPCODE_NAME = 'LIST_EXTEND'
    OPCODE_VALUE = 162

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LIST_EXTEND) {
        #     PyObject *iterable = POP();
        #     PyObject *list = PEEK(oparg);
        #     PyObject *none_val = _PyList_Extend((PyListObject *)list, iterable);
        #     if (none_val == NULL) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_TypeError) &&
        #            (Py_TYPE(iterable)->tp_iter == NULL && !PySequence_Check(iterable)))
        #         {
        #             _PyErr_Clear(tstate);
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                   "Value after * must be an iterable, not %.200s",
        #                   Py_TYPE(iterable)->tp_name);
        #         }
        #         Py_DECREF(iterable);
        #         goto error;
        #     }
        #     Py_DECREF(none_val);
        #     Py_DECREF(iterable);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
