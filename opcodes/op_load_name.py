# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadName(OpCode):
    """
    Pushes the value associated with co_names[namei] onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_NAME
    """
    name = 'LOAD_NAME'
    value = 101

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_NAME, ( -- v)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *locals = LOCALS();
        #     if (locals == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals when loading %R", name);
        #         goto error;
        #     }
        #     if (PyDict_CheckExact(locals)) {
        #         v = PyDict_GetItemWithError(locals, name);
        #         if (v != NULL) {
        #             Py_INCREF(v);
        #         }
        #         else if (_PyErr_Occurred(tstate)) {
        #             goto error;
        #         }
        #     }
        #     else {
        #         v = PyObject_GetItem(locals, name);
        #         if (v == NULL) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_KeyError))
        #                 goto error;
        #             _PyErr_Clear(tstate);
        #         }
        #     }
        #     if (v == NULL) {
        #         v = PyDict_GetItemWithError(GLOBALS(), name);
        #         if (v != NULL) {
        #             Py_INCREF(v);
        #         }
        #         else if (_PyErr_Occurred(tstate)) {
        #             goto error;
        #         }
        #         else {
        #             if (PyDict_CheckExact(BUILTINS())) {
        #                 v = PyDict_GetItemWithError(BUILTINS(), name);
        #                 if (v == NULL) {
        #                     if (!_PyErr_Occurred(tstate)) {
        #                         format_exc_check_arg(
        #                                 tstate, PyExc_NameError,
        #                                 NAME_ERROR_MSG, name);
        #                     }
        #                     goto error;
        #                 }
        #                 Py_INCREF(v);
        #             }
        #             else {
        #                 v = PyObject_GetItem(BUILTINS(), name);
        #                 if (v == NULL) {
        #                     if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                         format_exc_check_arg(
        #                                     tstate, PyExc_NameError,
        #                                     NAME_ERROR_MSG, name);
        #                     }
        #                     goto error;
        #                 }
        #             }
        #         }
        #     }
        # }
        name = cls.frame.get_name(oparg)
        locals = cls.frame.get_locals()
        if locals == None:
            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_SystemError,
                          "no locals when loading %R", name)
            cls.flow.error()
        if cls.api.PyDict_CheckExact(locals):
            v = cls.api.PyDict_GetItemWithError(locals, name)
            if v != None:
                cls.memory.inc_ref(v)
            elif cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.flow.error()
        else:
            v = cls.api.PyObject_GetItem(locals, name)
            if v == None:
                if not cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                    cls.flow.error()
                cls.api.private.PyErr_Clear(cls.frame.state)
        if v == None:
            v = cls.api.PyDict_GetItemWithError(cls.frame.get_globals(), name)
            if v != None:
                cls.memory.inc_ref(v)
            elif cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.flow.error()
            else:
                if cls.api.PyDict_CheckExact(cls.frame.get_builtins()):
                    v = cls.api.PyDict_GetItemWithError(cls.frame.get_builtins(), name)
                    if v == None:
                        if not cls.api.private.PyErr_Occurred(cls.frame.state):
                            format_exc_check_arg(
                                    cls.frame.state, cls.api.PyExc_NameError,
                                    NAME_ERROR_MSG, name)
                        cls.flow.error()
                    cls.memory.inc_ref(v)
                else:
                    v = cls.api.PyObject_GetItem(cls.frame.get_builtins(), name)
                    if v == None:
                        if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                            format_exc_check_arg(
                                        cls.frame.state, cls.api.PyExc_NameError,
                                        NAME_ERROR_MSG, name)
                        cls.flow.error()
        cls.stack.grow(1)
        cls.stack.poke(1, v)
        cls.flow.dispatch()
