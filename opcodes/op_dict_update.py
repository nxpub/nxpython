# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDictUpdate(OpCode):
    """
    Calls dict.update(TOS1[-i], TOS).  Used to build dicts.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-DICT_UPDATE
    """
    name = 'DICT_UPDATE'
    value = 165

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DICT_UPDATE, (update --)) {
        #     PyObject *dict = PEEK(oparg + 1);  // update is still on the stack
        #     if (PyDict_Update(dict, update) < 0) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_AttributeError)) {
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                             "'%.200s' object is not a mapping",
        #                             Py_TYPE(update)->tp_name);
        #         }
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     DECREF_INPUTS();
        # }
        update = cls.stack.peek(1)
        dict = cls.stack.peek(oparg + 1)  # update is still on the stack
        if cls.api.PyDict_Update(dict, update) < 0:
            if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_AttributeError):
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                                "'%.200s' object is not a mapping",
                                cls.api.Py_TYPE(update).tp_name)
            cls.memory.dec_ref(update)
            cls.flow.error_if(True, 1)
        cls.memory.dec_ref(update)
        cls.stack.shrink(1)
        cls.flow.dispatch()
