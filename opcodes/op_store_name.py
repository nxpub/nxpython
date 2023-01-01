# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreName(OpCode):
    """
    Implements name = TOS. namei is the index of name in the attribute
    co_names of the code object. The compiler tries to use
    STORE_FAST or STORE_GLOBAL if possible.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_NAME
    """
    name = 'STORE_NAME'
    value = 90

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_NAME, (v -- )) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *ns = LOCALS();
        #     int err;
        #     if (ns == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals found when storing %R", name);
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     if (PyDict_CheckExact(ns))
        #         err = PyDict_SetItem(ns, name, v);
        #     else
        #         err = PyObject_SetItem(ns, name, v);
        #     DECREF_INPUTS();
        #     ERROR_IF(err, error);
        # }
        v = cls.stack.peek(1)
        name = cls.frame.get_name(oparg)
        ns = cls.frame.get_locals()
        if ns == None:
            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_SystemError,
                          "no locals found when storing %R", name)
            cls.memory.dec_ref(v)
            cls.flow.error_if(True, 1)
        if cls.api.PyDict_CheckExact(ns):
            err = cls.api.PyDict_SetItem(ns, name, v)
        else:
            err = cls.api.PyObject_SetItem(ns, name, v)
        cls.memory.dec_ref(v)
        cls.flow.error_if(err, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
