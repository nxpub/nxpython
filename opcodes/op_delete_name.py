# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteName(OpCode):
    """
    Implements del name, where namei is the index into co_names
    attribute of the code object.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_NAME
    """
    name = 'DELETE_NAME'
    value = 91

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DELETE_NAME, (--)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *ns = LOCALS();
        #     int err;
        #     if (ns == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals when deleting %R", name);
        #         goto error;
        #     }
        #     err = PyObject_DelItem(ns, name);
        #     // Can't use ERROR_IF here.
        #     if (err != 0) {
        #         format_exc_check_arg(tstate, PyExc_NameError,
        #                              NAME_ERROR_MSG,
        #                              name);
        #         goto error;
        #     }
        # }
        name = cls.frame.get_name(oparg)
        ns = cls.frame.get_locals()
        if ns == None:
            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_SystemError,
                          "no locals when deleting %R", name)
            cls.flow.error()
        err = cls.api.PyObject_DelItem(ns, name)
        # Can't use ERROR_IF here.
        if err != 0:
            format_exc_check_arg(cls.frame.state, cls.api.PyExc_NameError,
                                 NAME_ERROR_MSG,
                                 name)
            cls.flow.error()
        cls.flow.dispatch()
