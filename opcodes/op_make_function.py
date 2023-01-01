# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpMakeFunction(OpCode):
    """
    Pushes a new function object on the stack.  From bottom to top, the consumed
    stack must consist of values if the argument carries a specified flag value
    
    0x01 a tuple of default values for positional-only and
    positional-or-keyword parameters in positional order
    
    0x02 a dictionary of keyword-only parameters’ default values
    
    0x04 a tuple of strings containing parameters’ annotations
    
    0x08 a tuple containing cells for free variables, making a closure
    
    the code associated with the function (at TOS1)
    
    the qualified name of the function (at TOS)
    
    Changed in version 3.10: Flag value 0x04 is a tuple of strings instead of dictionary

    https://docs.python.org/3.12/library/dis.html#opcode-MAKE_FUNCTION
    """
    name = 'MAKE_FUNCTION'
    value = 132

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: MAKE_FUNCTION has irregular stack effect
        # inst(MAKE_FUNCTION) {
        #     PyObject *codeobj = POP();
        #     PyFunctionObject *func = (PyFunctionObject *)
        #         PyFunction_New(codeobj, GLOBALS());

        #     Py_DECREF(codeobj);
        #     if (func == NULL) {
        #         goto error;
        #     }

        #     if (oparg & 0x08) {
        #         assert(PyTuple_CheckExact(TOP()));
        #         func->func_closure = POP();
        #     }
        #     if (oparg & 0x04) {
        #         assert(PyTuple_CheckExact(TOP()));
        #         func->func_annotations = POP();
        #     }
        #     if (oparg & 0x02) {
        #         assert(PyDict_CheckExact(TOP()));
        #         func->func_kwdefaults = POP();
        #     }
        #     if (oparg & 0x01) {
        #         assert(PyTuple_CheckExact(TOP()));
        #         func->func_defaults = POP();
        #     }

        #     func->func_version = ((PyCodeObject *)codeobj)->co_version;
        #     PUSH((PyObject *)func);
        # }
        codeobj = cls.stack.pop()
        func = (cls.api.PyFunctionObject *)
            cls.api.PyFunction_New(codeobj, cls.frame.get_globals())

        cls.memory.dec_ref(codeobj)
        if func == None:
            cls.flow.error()

        if oparg & 0x08:
            # assert(PyTuple_CheckExact(TOP()))
            func.func_closure = cls.stack.pop()
        if oparg & 0x04:
            # assert(PyTuple_CheckExact(TOP()))
            func.func_annotations = cls.stack.pop()
        if oparg & 0x02:
            # assert(PyDict_CheckExact(TOP()))
            func.func_kwdefaults = cls.stack.pop()
        if oparg & 0x01:
            # assert(PyTuple_CheckExact(TOP()))
            func.func_defaults = cls.stack.pop()

        func.func_version = (codeobj).co_version
        cls.stack.push(func)
        cls.flow.dispatch()
