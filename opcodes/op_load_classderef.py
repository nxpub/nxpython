# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadClassderef(OpCode):
    """
    Much like LOAD_DEREF but first checks the locals dictionary before
    consulting the cell.  This is used for loading free variables in class
    bodies.
    
    New in version 3.4.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CLASSDEREF
    """
    name = 'LOAD_CLASSDEREF'
    value = 148

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LOAD_CLASSDEREF, ( -- value)) {
        #     PyObject *name, *locals = LOCALS();
        #     assert(locals);
        #     assert(oparg >= 0 && oparg < frame->f_code->co_nlocalsplus);
        #     name = PyTuple_GET_ITEM(frame->f_code->co_localsplusnames, oparg);
        #     if (PyDict_CheckExact(locals)) {
        #         value = PyDict_GetItemWithError(locals, name);
        #         if (value != NULL) {
        #             Py_INCREF(value);
        #         }
        #         else if (_PyErr_Occurred(tstate)) {
        #             goto error;
        #         }
        #     }
        #     else {
        #         value = PyObject_GetItem(locals, name);
        #         if (value == NULL) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                 goto error;
        #             }
        #             _PyErr_Clear(tstate);
        #         }
        #     }
        #     if (!value) {
        #         PyObject *cell = GETLOCAL(oparg);
        #         value = PyCell_GET(cell);
        #         if (value == NULL) {
        #             format_exc_unbound(tstate, frame->f_code, oparg);
        #             goto error;
        #         }
        #         Py_INCREF(value);
        #     }
        # }
        name, *locals = cls.frame.get_locals()
        # assert(locals)
        # assert(oparg >= 0 && oparg < frame->f_code->co_nlocalsplus)
        name = cls.api.PyTuple_GET_ITEM(frame.f_code.co_localsplusnames, oparg)
        if cls.api.PyDict_CheckExact(locals):
            value = cls.api.PyDict_GetItemWithError(locals, name)
            if value != None:
                cls.memory.inc_ref(value)
            elif cls.api.private.PyErr_Occurred(cls.frame.state):
                cls.flow.error()
        else:
            value = cls.api.PyObject_GetItem(locals, name)
            if value == None:
                if not cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                    cls.flow.error()
                cls.api.private.PyErr_Clear(cls.frame.state)
        if not value:
            cell = cls.frame.get_local(oparg)
            value = cls.api.PyCell_GET(cell)
            if value == None:
                format_exc_unbound(cls.frame.state, frame.f_code, oparg)
                cls.flow.error()
            cls.memory.inc_ref(value)
        cls.stack.grow(1)
        cls.stack.poke(1, value)
        cls.flow.dispatch()
