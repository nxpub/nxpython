# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpGetAiter(OpCode):
    """
    Implements TOS = TOS.__aiter__().
    
    New in version 3.5.
    
    Changed in version 3.7: Returning awaitable objects from __aiter__ is no longer
    supported.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_AITER
    """
    OPCODE_NAME = 'GET_AITER'
    OPCODE_VALUE = 50

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, obj) -> None:
        # TARGET(GET_AITER) {
        #     PyObject *obj = PEEK(1);
        #     PyObject *iter;
        #     unaryfunc getter = NULL;
        #     PyTypeObject *type = Py_TYPE(obj);

        #     if (type->tp_as_async != NULL) {
        #         getter = type->tp_as_async->am_aiter;
        #     }

        #     if (getter == NULL) {
        #         _PyErr_Format(tstate, PyExc_TypeError,
        #                       "'async for' requires an object with "
        #                       "__aiter__ method, got %.100s",
        #                       type->tp_name);
        #         Py_DECREF(obj);
        #         if (true) goto pop_1_error;
        #     }

        #     iter = (*getter)(obj);
        #     Py_DECREF(obj);
        #     if (iter == NULL) goto pop_1_error;

        #     if (Py_TYPE(iter)->tp_as_async == NULL ||
        #             Py_TYPE(iter)->tp_as_async->am_anext == NULL) {

        #         _PyErr_Format(tstate, PyExc_TypeError,
        #                       "'async for' received an object from __aiter__ "
        #                       "that does not implement __anext__: %.100s",
        #                       Py_TYPE(iter)->tp_name);
        #         Py_DECREF(iter);
        #         if (true) goto pop_1_error;
        #     }
        #     POKE(1, iter);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
