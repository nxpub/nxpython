# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpGetYieldFromIter(BaseOpCode):
    """
    If TOS is a generator iterator or coroutine object
    it is left as is.  Otherwise, implements TOS = iter(TOS).
    
    New in version 3.5.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_YIELD_FROM_ITER
    """
    OPCODE_NAME = 'GET_YIELD_FROM_ITER'
    OPCODE_VALUE = 69

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(GET_YIELD_FROM_ITER) {
        #     /* before: [obj]; after [getiter(obj)] */
        #     PyObject *iterable = TOP();
        #     PyObject *iter;
        #     if (PyCoro_CheckExact(iterable)) {
        #         /* `iterable` is a coroutine */
        #         if (!(frame->f_code->co_flags & (CO_COROUTINE | CO_ITERABLE_COROUTINE))) {
        #             /* and it is used in a 'yield from' expression of a
        #                regular generator. */
        #             Py_DECREF(iterable);
        #             SET_TOP(NULL);
        #             _PyErr_SetString(tstate, PyExc_TypeError,
        #                              "cannot 'yield from' a coroutine object "
        #                              "in a non-coroutine generator");
        #             goto error;
        #         }
        #     }
        #     else if (!PyGen_CheckExact(iterable)) {
        #         /* `iterable` is not a generator. */
        #         iter = PyObject_GetIter(iterable);
        #         Py_DECREF(iterable);
        #         SET_TOP(iter);
        #         if (iter == NULL)
        #             goto error;
        #     }
        #     PREDICT(LOAD_CONST);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
