# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpLoadClassderef(OpCode):
    """
    Much like LOAD_DEREF but first checks the locals dictionary before
    consulting the cell.  This is used for loading free variables in class
    bodies.
    
    New in version 3.4.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CLASSDEREF
    """
    OPCODE_NAME = 'LOAD_CLASSDEREF'
    OPCODE_VALUE = 148

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_CLASSDEREF) {
        #     PyObject *name, *value, *locals = LOCALS();
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
        #     PUSH(value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
