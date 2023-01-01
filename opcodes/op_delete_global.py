# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteGlobal(OpCode):
    """
    Works as DELETE_NAME, but deletes a global name.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_GLOBAL
    """
    name = 'DELETE_GLOBAL'
    value = 98

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DELETE_GLOBAL, (--)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     int err;
        #     err = PyDict_DelItem(GLOBALS(), name);
        #     // Can't use ERROR_IF here.
        #     if (err != 0) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #             format_exc_check_arg(tstate, PyExc_NameError,
        #                                  NAME_ERROR_MSG, name);
        #         }
        #         goto error;
        #     }
        # }
        name = cls.frame.get_name(oparg)
        err = cls.api.PyDict_DelItem(cls.frame.get_globals(), name)
        # Can't use ERROR_IF here.
        if err != 0:
            if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                format_exc_check_arg(cls.frame.state, cls.api.PyExc_NameError,
                                     NAME_ERROR_MSG, name)
            cls.flow.error()
        cls.flow.dispatch()
