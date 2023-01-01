# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpGetAiter(OpCode):
    """
    Implements TOS = TOS.__aiter__().
    
    New in version 3.5.
    
    Changed in version 3.7: Returning awaitable objects from __aiter__ is no longer
    supported.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_AITER
    """
    name = 'GET_AITER'
    value = 50

    @classmethod
    def logic(cls) -> None:
        # inst(GET_AITER, (obj -- iter)) {
        #     unaryfunc getter = NULL;
        #     PyTypeObject *type = Py_TYPE(obj);

        #     if (type->tp_as_async != NULL) {
        #         getter = type->tp_as_async->am_aiter;
        #     }

        #     if (getter == NULL) {
        #         _PyErr_Format(tstate, PyExc_TypeError,
        #                       "'async for' requires an object with "
        #                       "__aiter__ method, got %.100s",
        #                       type->tp_name);
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }

        #     iter = (*getter)(obj);
        #     DECREF_INPUTS();
        #     ERROR_IF(iter == NULL, error);

        #     if (Py_TYPE(iter)->tp_as_async == NULL ||
        #             Py_TYPE(iter)->tp_as_async->am_anext == NULL) {

        #         _PyErr_Format(tstate, PyExc_TypeError,
        #                       "'async for' received an object from __aiter__ "
        #                       "that does not implement __anext__: %.100s",
        #                       Py_TYPE(iter)->tp_name);
        #         Py_DECREF(iter);
        #         ERROR_IF(true, error);
        #     }
        # }
        obj = cls.stack.peek(1)
        getter = None
        type = cls.api.Py_TYPE(obj)

        if type.tp_as_async != None:
            getter = type.tp_as_async.am_aiter

        if getter == None:
            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                          "'async for' requires an object with "
                          "__aiter__ method, got %.100s",
                          type.tp_name)
            cls.memory.dec_ref(obj)
            cls.flow.error_if(True, 1)

        iter = (*getter)(obj)
        cls.memory.dec_ref(obj)
        cls.flow.error_if(iter == None, 1)

        if cls.api.Py_TYPE(iter:.tp_as_async == None ||
                cls.api.Py_TYPE(iter).tp_as_async.am_anext == None) {

            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_TypeError,
                          "'async for' received an object from __aiter__ "
                          "that does not implement __anext__: %.100s",
                          cls.api.Py_TYPE(iter).tp_name)
            cls.memory.dec_ref(iter)
            cls.flow.error_if(True, 1)
        cls.stack.poke(1, iter)
        cls.flow.dispatch()
