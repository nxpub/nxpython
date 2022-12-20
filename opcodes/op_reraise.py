# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpReraise(BaseOpCode):
    """
    Re-raises the exception currently on top of the stack. If oparg is non-zero,
    pops an additional value from the stack which is used to set f_lasti
    of the current frame.
    
    New in version 3.9.
    
    Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-RERAISE
    """
    OPCODE_NAME = 'RERAISE'
    OPCODE_VALUE = 119

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(RERAISE) {
        #     if (oparg) {
        #         PyObject *lasti = PEEK(oparg + 1);
        #         if (PyLong_Check(lasti)) {
        #             frame->prev_instr = _PyCode_CODE(frame->f_code) + PyLong_AsLong(lasti);
        #             assert(!_PyErr_Occurred(tstate));
        #         }
        #         else {
        #             assert(PyLong_Check(lasti));
        #             _PyErr_SetString(tstate, PyExc_SystemError, "lasti is not an int");
        #             goto error;
        #         }
        #     }
        #     PyObject *val = POP();
        #     assert(val && PyExceptionInstance_Check(val));
        #     PyObject *exc = Py_NewRef(PyExceptionInstance_Class(val));
        #     PyObject *tb = PyException_GetTraceback(val);
        #     _PyErr_Restore(tstate, exc, val, tb);
        #     goto exception_unwind;
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
