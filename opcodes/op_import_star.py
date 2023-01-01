# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpImportStar(OpCode):
    """
    Loads all symbols not starting with '_' directly from the module TOS to
    the local namespace. The module is popped after loading all names. This
    opcode implements from module import *.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_STAR
    """
    name = 'IMPORT_STAR'
    value = 84

    @classmethod
    def logic(cls) -> None:
        # inst(IMPORT_STAR, (from --)) {
        #     PyObject *locals;
        #     int err;
        #     if (_PyFrame_FastToLocalsWithError(frame) < 0) {
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }

        #     locals = LOCALS();
        #     if (locals == NULL) {
        #         _PyErr_SetString(tstate, PyExc_SystemError,
        #                          "no locals found during 'import *'");
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     err = import_all_from(tstate, locals, from);
        #     _PyFrame_LocalsToFast(frame, 0);
        #     DECREF_INPUTS();
        #     ERROR_IF(err, error);
        # }
        from = cls.stack.peek(1)
        if cls.api.private.PyFrame_FastToLocalsWithError(frame) < 0:
            cls.memory.dec_ref(from)
            cls.flow.error_if(True, 1)

        locals = cls.frame.get_locals()
        if locals == None:
            cls.api.private.PyErr_SetString(cls.frame.state, cls.api.PyExc_SystemError,
                             "no locals found during 'import *'")
            cls.memory.dec_ref(from)
            cls.flow.error_if(True, 1)
        err = import_all_from(cls.frame.state, locals, from)
        cls.api.private.PyFrame_LocalsToFast(frame, 0)
        cls.memory.dec_ref(from)
        cls.flow.error_if(err, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
