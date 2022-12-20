# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpGetAwaitable(BaseOpCode):
    """
    Implements TOS = get_awaitable(TOS), where get_awaitable(o)
    returns o if o is a coroutine object or a generator object with
    the CO_ITERABLE_COROUTINE flag, or resolves
    o.__await__.
    
    If the where operand is nonzero, it indicates where the instruction
    occurs:
    
    1 After a call to __aenter__
    
    2 After a call to __aexit__
    
    New in version 3.5.
    
    Changed in version 3.11: Previously, this instruction did not have an oparg.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_AWAITABLE
    """
    OPCODE_NAME = 'GET_AWAITABLE'
    OPCODE_VALUE = 131

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(GET_AWAITABLE) {
        #     PREDICTED(GET_AWAITABLE);
        #     PyObject *iterable = TOP();
        #     PyObject *iter = _PyCoro_GetAwaitableIter(iterable);

        #     if (iter == NULL) {
        #         format_awaitable_error(tstate, Py_TYPE(iterable), oparg);
        #     }

        #     Py_DECREF(iterable);

        #     if (iter != NULL && PyCoro_CheckExact(iter)) {
        #         PyObject *yf = _PyGen_yf((PyGenObject*)iter);
        #         if (yf != NULL) {
        #             /* `iter` is a coroutine object that is being
        #                awaited, `yf` is a pointer to the current awaitable
        #                being awaited on. */
        #             Py_DECREF(yf);
        #             Py_CLEAR(iter);
        #             _PyErr_SetString(tstate, PyExc_RuntimeError,
        #                              "coroutine is being awaited already");
        #             /* The code below jumps to `error` if `iter` is NULL. */
        #         }
        #     }

        #     SET_TOP(iter); /* Even if it's NULL */

        #     if (iter == NULL) {
        #         goto error;
        #     }

        #     PREDICT(LOAD_CONST);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
