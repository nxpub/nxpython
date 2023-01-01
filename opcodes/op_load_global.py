# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadGlobal(OpCode):
    """
    Loads the global named co_names[namei>>1] onto the stack.
    
    Changed in version 3.11: If the low bit of namei is set, then a NULL is pushed to the
    stack before the global variable.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_GLOBAL
    """
    name = 'LOAD_GLOBAL'
    value = 116

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: LOAD_GLOBAL has irregular stack effect
        # inst(LOAD_GLOBAL) {
        #     _PyLoadGlobalCache *cache = (_PyLoadGlobalCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         PyObject *name = GETITEM(names, oparg>>1);
        #         next_instr--;
        #         _Py_Specialize_LoadGlobal(GLOBALS(), BUILTINS(), next_instr, name);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(LOAD_GLOBAL, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     int push_null = oparg & 1;
        #     PEEK(0) = NULL;
        #     PyObject *name = GETITEM(names, oparg>>1);
        #     PyObject *v;
        #     if (PyDict_CheckExact(GLOBALS())
        #         && PyDict_CheckExact(BUILTINS()))
        #     {
        #         v = _PyDict_LoadGlobal((PyDictObject *)GLOBALS(),
        #                                (PyDictObject *)BUILTINS(),
        #                                name);
        #         if (v == NULL) {
        #             if (!_PyErr_Occurred(tstate)) {
        #                 /* _PyDict_LoadGlobal() returns NULL without raising
        #                  * an exception if the key doesn't exist */
        #                 format_exc_check_arg(tstate, PyExc_NameError,
        #                                      NAME_ERROR_MSG, name);
        #             }
        #             goto error;
        #         }
        #         Py_INCREF(v);
        #     }
        #     else {
        #         /* Slow-path if globals or builtins is not a dict */

        #         /* namespace 1: globals */
        #         v = PyObject_GetItem(GLOBALS(), name);
        #         if (v == NULL) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                 goto error;
        #             }
        #             _PyErr_Clear(tstate);

        #             /* namespace 2: builtins */
        #             v = PyObject_GetItem(BUILTINS(), name);
        #             if (v == NULL) {
        #                 if (_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                     format_exc_check_arg(
        #                                 tstate, PyExc_NameError,
        #                                 NAME_ERROR_MSG, name);
        #                 }
        #                 goto error;
        #             }
        #         }
        #     }
        #     /* Skip over inline cache */
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_GLOBAL);
        #     STACK_GROW(push_null);
        #     PUSH(v);
        # }
        push_null = oparg & 1
        cls.stack.peek(0) = None
        name = cls.frame.get_name(oparg>>1)
        if cls.api.PyDict_CheckExact(cls.frame.get_globals():
            and cls.api.PyDict_CheckExact(cls.frame.get_builtins()))
        {
            v = cls.api.private.PyDict_LoadGlobal(cls.frame.get_globals(),
                                   cls.frame.get_builtins(),
                                   name)
            if v == None:
                if not cls.api.private.PyErr_Occurred(cls.frame.state):
                    # _PyDict_LoadGlobal() returns NULL without raising
        #              * an exception if the key doesn't exist 
                    format_exc_check_arg(cls.frame.state, cls.api.PyExc_NameError,
                                         NAME_ERROR_MSG, name)
                cls.flow.error()
            cls.memory.inc_ref(v)
        else:
            # Slow-path if globals or builtins is not a dict 

            # namespace 1: globals 
            v = cls.api.PyObject_GetItem(cls.frame.get_globals(), name)
            if v == None:
                if not cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                    cls.flow.error()
                cls.api.private.PyErr_Clear(cls.frame.state)

                # namespace 2: builtins 
                v = cls.api.PyObject_GetItem(cls.frame.get_builtins(), name)
                if v == None:
                    if cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError):
                        format_exc_check_arg(
                                    cls.frame.state, cls.api.PyExc_NameError,
                                    NAME_ERROR_MSG, name)
                    cls.flow.error()
        # Skip over inline cache 
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_LOAD_GLOBAL)
        cls.stack.grow(push_null)
        cls.stack.push(v)
        cls.flow.dispatch()
