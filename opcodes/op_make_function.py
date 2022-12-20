# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMakeFunction(BaseOpCode):
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
    OPCODE_NAME = 'MAKE_FUNCTION'
    OPCODE_VALUE = 132

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MAKE_FUNCTION) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
