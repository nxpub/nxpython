# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadBuildClass(OpCode):
    """
    Pushes builtins.__build_class__() onto the stack.  It is later called
    to construct a class.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_BUILD_CLASS
    """
    name = 'LOAD_BUILD_CLASS'
    value = 71

    @classmethod
    def logic(cls) -> None:
        # inst(LOAD_BUILD_CLASS, ( -- bc)) {
        #     if (PyDict_CheckExact(BUILTINS())) {
        #         bc = _PyDict_GetItemWithError(BUILTINS(),
        #                                       &_Py_ID(__build_class__));
        #         if (bc == NULL) {
        #             if (!_PyErr_Occurred(tstate)) {
        #                 _PyErr_SetString(tstate, PyExc_NameError,
        #                                  "__build_class__ not found");
        #             }
        #             ERROR_IF(true, error);
        #         }
        #         Py_INCREF(bc);
        #     }
        #     else {
        #         bc = PyObject_GetItem(BUILTINS(), &_Py_ID(__build_class__));
        #         if (bc == NULL) {
        #             if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError))
        #                 _PyErr_SetString(tstate, PyExc_NameError,
        #                                  "__build_class__ not found");
        #             ERROR_IF(true, error);
        #         }
        #     }
        # }
        if cls.api.PyDict_CheckExact(cls.frame.get_builtins()):
            bc = cls.api.private.PyDict_GetItemWithError(cls.frame.get_builtins(),
                                          cls.api.private.Py_ID('__build_class__'))
            if bc == None:
                if not cls.api.private.PyErr_Occurred(cls.frame.state):
                    cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_NameError,
                                     "__build_class__ not found")
                cls.flow.error_if(True)
            cls.memory.inc_ref(bc)
        else:
            bc = cls.api.PyObject_GetItem(cls.frame.get_builtins(), cls.api.private.Py_ID('__build_class__'))
            if bc == None:
                if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                    cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_NameError,
                                     "__build_class__ not found")
                cls.flow.error_if(True)
        cls.stack.grow(1)
        cls.stack.poke(1, bc)
        cls.flow.dispatch()
