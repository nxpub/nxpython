# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpRaiseVarargs(OpCode):
    """
    Raises an exception using one of the 3 forms of the raise statement,
    depending on the value of argc:
    
    0: raise (re-raise previous exception)
    
    1: raise TOS (raise exception instance or type at TOS)
    
    2: raise TOS1 from TOS (raise exception instance or type at TOS1
    with __cause__ set to TOS)

    https://docs.python.org/3.12/library/dis.html#opcode-RAISE_VARARGS
    """
    name = 'RAISE_VARARGS'
    value = 130

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- )
        # inst(RAISE_VARARGS) {
        #     PyObject *cause = NULL, *exc = NULL;
        #     switch (oparg) {
        #     case 2:
        #         cause = POP(); /* cause */
        #         /* fall through */
        #     case 1:
        #         exc = POP(); /* exc */
        #         /* fall through */
        #     case 0:
        #         if (do_raise(tstate, exc, cause)) {
        #             goto exception_unwind;
        #         }
        #         break;
        #     default:
        #         _PyErr_SetString(tstate, PyExc_SystemError,
        #                          "bad RAISE_VARARGS oparg");
        #         break;
        #     }
        #     goto error;
        # }
        cause = None, *exc = None
        switch (oparg) {
        case 2:
        #     cause = POP() /* cause 
            # fall through 
        case 1:
        #     exc = POP() /* exc 
            # fall through 
        case 0:
            if do_raise(cls.frame.state, exc, cause):
                cls.flow.exception_unwind()
            break
        default:
            cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_SystemError,
                             "bad RAISE_VARARGS oparg")
            break
        cls.flow.error()
