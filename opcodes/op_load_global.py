# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadGlobal(BaseOpCode):
    """
    Loads the global named co_names[namei>>1] onto the stack.
    
    Changed in version 3.11: If the low bit of namei is set, then a NULL is pushed to the
    stack before the global variable.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_GLOBAL
    """
    OPCODE_NAME = 'LOAD_GLOBAL'
    OPCODE_VALUE = 116

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_GLOBAL) {
        #     PREDICTED(LOAD_GLOBAL);
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
