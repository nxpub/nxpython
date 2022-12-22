# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpPrintExpr(OpCode):
    """
    Implements the expression statement for the interactive mode.  TOS is removed
    from the stack and printed.  In non-interactive mode, an expression statement
    is terminated with POP_TOP.

    https://docs.python.org/3.12/library/dis.html#opcode-PRINT_EXPR
    """
    OPCODE_NAME = 'PRINT_EXPR'
    OPCODE_VALUE = 70

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, value) -> None:
        # TARGET(PRINT_EXPR) {
        #     PyObject *value = PEEK(1);
        #     PyObject *hook = _PySys_GetAttr(tstate, &_Py_ID(displayhook));
        #     PyObject *res;
        #     // Can't use ERROR_IF here.
        #     if (hook == NULL) {
        #         _PyErr_SetString(tstate, PyExc_RuntimeError,
        #                          "lost sys.displayhook");
        #         Py_DECREF(value);
        #         if (true) goto pop_1_error;
        #     }
        #     res = PyObject_CallOneArg(hook, value);
        #     Py_DECREF(value);
        #     if (res == NULL) goto pop_1_error;
        #     Py_DECREF(res);
        #     STACK_SHRINK(1);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
