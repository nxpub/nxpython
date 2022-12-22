# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpGetAnext(OpCode):
    """
    Pushes get_awaitable(TOS.__anext__()) to the stack.  See
    GET_AWAITABLE for details about get_awaitable.
    
    New in version 3.5.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_ANEXT
    """
    OPCODE_NAME = 'GET_ANEXT'
    OPCODE_VALUE = 51

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(GET_ANEXT) {
        #     unaryfunc getter = NULL;
        #     PyObject *next_iter = NULL;
        #     PyObject *awaitable = NULL;
        #     PyObject *aiter = TOP();
        #     PyTypeObject *type = Py_TYPE(aiter);

        #     if (PyAsyncGen_CheckExact(aiter)) {
        #         awaitable = type->tp_as_async->am_anext(aiter);
        #         if (awaitable == NULL) {
        #             goto error;
        #         }
        #     } else {
        #         if (type->tp_as_async != NULL){
        #             getter = type->tp_as_async->am_anext;
        #         }

        #         if (getter != NULL) {
        #             next_iter = (*getter)(aiter);
        #             if (next_iter == NULL) {
        #                 goto error;
        #             }
        #         }
        #         else {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                           "'async for' requires an iterator with "
        #                           "__anext__ method, got %.100s",
        #                           type->tp_name);
        #             goto error;
        #         }

        #         awaitable = _PyCoro_GetAwaitableIter(next_iter);
        #         if (awaitable == NULL) {
        #             _PyErr_FormatFromCause(
        #                 PyExc_TypeError,
        #                 "'async for' received an invalid object "
        #                 "from __anext__: %.100s",
        #                 Py_TYPE(next_iter)->tp_name);

        #             Py_DECREF(next_iter);
        #             goto error;
        #         } else {
        #             Py_DECREF(next_iter);
        #         }
        #     }

        #     PUSH(awaitable);
        #     PREDICT(LOAD_CONST);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
