# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreName(BaseOpCode):
    """
    Implements name = TOS. namei is the index of name in the attribute
    co_names of the code object. The compiler tries to use
    STORE_FAST or STORE_GLOBAL if possible.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_NAME
    """
    OPCODE_NAME = 'STORE_NAME'
    OPCODE_VALUE = 90

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(STORE_NAME) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *v = POP();
        #     PyObject *ns = LOCALS();
        #     int err;
        #     if (ns == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals found when storing %R", name);
        #         Py_DECREF(v);
        #         goto error;
        #     }
        #     if (PyDict_CheckExact(ns))
        #         err = PyDict_SetItem(ns, name, v);
        #     else
        #         err = PyObject_SetItem(ns, name, v);
        #     Py_DECREF(v);
        #     if (err != 0)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
