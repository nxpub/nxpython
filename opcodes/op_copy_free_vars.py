# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCopyFreeVars(BaseOpCode):
    """
    Copies the n free variables from the closure into the frame.
    Removes the need for special code on the caller’s side when calling
    closures.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-COPY_FREE_VARS
    """
    OPCODE_NAME = 'COPY_FREE_VARS'
    OPCODE_VALUE = 149

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(COPY_FREE_VARS) {
        #     /* Copy closure variables to free variables */
        #     PyCodeObject *co = frame->f_code;
        #     assert(PyFunction_Check(frame->f_funcobj));
        #     PyObject *closure = ((PyFunctionObject *)frame->f_funcobj)->func_closure;
        #     int offset = co->co_nlocals + co->co_nplaincellvars;
        #     assert(oparg == co->co_nfreevars);
        #     for (int i = 0; i < oparg; ++i) {
        #         PyObject *o = PyTuple_GET_ITEM(closure, i);
        #         frame->localsplus[offset + i] = Py_NewRef(o);
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
