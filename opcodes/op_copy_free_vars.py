# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCopyFreeVars(OpCode):
    """
    Copies the n free variables from the closure into the frame.
    Removes the need for special code on the caller’s side when calling
    closures.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-COPY_FREE_VARS
    """
    name = 'COPY_FREE_VARS'
    value = 149

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(COPY_FREE_VARS, (--)) {
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
        # }
        # Copy closure variables to free variables 
        co = frame.f_code
        # assert(PyFunction_Check(frame->f_funcobj))
        closure = (frame.f_funcobj).func_closure
        offset = co.co_nlocals + co.co_nplaincellvars
        # assert(oparg == co->co_nfreevars)
        for (int i = 0 i < oparg ++i) {
            o = cls.api.PyTuple_GET_ITEM(closure, i)
            frame.localsplus[offset + i] = cls.api.Py_NewRef(o)
        cls.flow.dispatch()
