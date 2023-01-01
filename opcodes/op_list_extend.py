# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpListExtend(OpCode):
    """
    Calls list.extend(TOS1[-i], TOS).  Used to build lists.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-LIST_EXTEND
    """
    name = 'LIST_EXTEND'
    value = 162

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(LIST_EXTEND, (iterable -- )) {
        #     PyObject *list = PEEK(oparg + 1);  // iterable is still on the stack
        #     PyObject *none_val = _PyList_Extend((PyListObject *)list, iterable);
        #     if (none_val == NULL) {
        #         if (_PyErr_ExceptionMatches(tstate, PyExc_TypeError) &&
        #            (Py_TYPE(iterable)->tp_iter == NULL && !PySequence_Check(iterable)))
        #         {
        #             _PyErr_Clear(tstate);
        #             _PyErr_Format(tstate, PyExc_TypeError,
        #                   "Value after * must be an iterable, not %.200s",
        #                   Py_TYPE(iterable)->tp_name);
        #         }
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     Py_DECREF(none_val);
        #     DECREF_INPUTS();
        # }
        iterable = cls.stack.peek(1)
        list = cls.stack.peek(oparg + 1)  # iterable is still on the stack
        none_val = cls.api.private.PyList_Extend(list, iterable)
        if none_val == None:
            if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_TypeError:&&
               (cls.api.Py_TYPE(iterable).tp_iter == None and not cls.api.PySequence_Check(iterable)))
            {
                cls.api.private.PyErr_Clear(cls.frame.state)
                cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                      "Value after * must be an iterable, not %.200s",
                      cls.api.Py_TYPE(iterable).tp_name)
            cls.memory.dec_ref(iterable)
            cls.flow.error_if(True, 1)
        cls.memory.dec_ref(none_val)
        cls.memory.dec_ref(iterable)
        cls.stack.shrink(1)
        cls.flow.dispatch()
