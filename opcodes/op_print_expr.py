# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpPrintExpr(OpCode):
    """
    Implements the expression statement for the interactive mode.  TOS is removed
    from the stack and printed.  In non-interactive mode, an expression statement
    is terminated with POP_TOP.

    https://docs.python.org/3.12/library/dis.html#opcode-PRINT_EXPR
    """
    name = 'PRINT_EXPR'
    value = 70

    @classmethod
    def logic(cls) -> None:
        # inst(PRINT_EXPR, (value --)) {
        #     PyObject *hook = _PySys_GetAttr(tstate, &_Py_ID(displayhook));
        #     PyObject *res;
        #     // Can't use ERROR_IF here.
        #     if (hook == NULL) {
        #         _PyErr_SetString(tstate, PyExc_RuntimeError,
        #                          "lost sys.displayhook");
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     res = PyObject_CallOneArg(hook, value);
        #     DECREF_INPUTS();
        #     ERROR_IF(res == NULL, error);
        #     Py_DECREF(res);
        # }
        value = cls.stack.peek(1)
        hook = cls.api.private.PySys_GetAttr(cls.frame.state, cls.api.private.Py_ID('displayhook'))
        # Can't use ERROR_IF here.
        if hook == None:
            cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_RuntimeError,
                             "lost sys.displayhook")
            cls.memory.dec_ref(value)
            cls.flow.error_if(True, 1)
        res = cls.api.PyObject_CallOneArg(hook, value)
        cls.memory.dec_ref(value)
        cls.flow.error_if(res == None, 1)
        cls.memory.dec_ref(res)
        cls.stack.shrink(1)
        cls.flow.dispatch()
