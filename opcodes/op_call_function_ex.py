# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallFunctionEx(OpCode):
    """
    Calls a callable object with variable set of positional and keyword
    arguments.  If the lowest bit of flags is set, the top of the stack
    contains a mapping object containing additional keyword arguments.
    Before the callable is called, the mapping object and iterable object
    are each “unpacked” and their contents passed in as keyword and
    positional arguments respectively.
    CALL_FUNCTION_EX pops all arguments and the callable object off the stack,
    calls the callable object with those arguments, and pushes the return value
    returned by the callable object.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-CALL_FUNCTION_EX
    """
    OPCODE_NAME = 'CALL_FUNCTION_EX'
    OPCODE_VALUE = 142

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_FUNCTION_EX) {
        #     PREDICTED(CALL_FUNCTION_EX);
        #     PyObject *func, *callargs, *kwargs = NULL, *result;
        #     if (oparg & 0x01) {
        #         kwargs = POP();
        #         // DICT_MERGE is called before this opcode if there are kwargs.
        #         // It converts all dict subtypes in kwargs into regular dicts.
        #         assert(PyDict_CheckExact(kwargs));
        #     }
        #     callargs = POP();
        #     func = TOP();
        #     if (!PyTuple_CheckExact(callargs)) {
        #         if (check_args_iterable(tstate, func, callargs) < 0) {
        #             Py_DECREF(callargs);
        #             goto error;
        #         }
        #         Py_SETREF(callargs, PySequence_Tuple(callargs));
        #         if (callargs == NULL) {
        #             goto error;
        #         }
        #     }
        #     assert(PyTuple_CheckExact(callargs));

        #     result = do_call_core(tstate, func, callargs, kwargs, cframe.use_tracing);
        #     Py_DECREF(func);
        #     Py_DECREF(callargs);
        #     Py_XDECREF(kwargs);

        #     STACK_SHRINK(1);
        #     assert(TOP() == NULL);
        #     SET_TOP(result);
        #     if (result == NULL) {
        #         goto error;
        #     }
        #     CHECK_EVAL_BREAKER();
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
