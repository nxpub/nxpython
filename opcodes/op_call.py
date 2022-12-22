# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCall(OpCode):
    """
    Calls a callable object with the number of arguments specified by argc,
    including the named arguments specified by the preceding
    KW_NAMES, if any.
    On the stack are (in ascending order), either:
    
    NULL
    
    The callable
    
    The positional arguments
    
    The named arguments
    
    or:
    
    The callable
    
    self
    
    The remaining positional arguments
    
    The named arguments
    
    argc is the total of the positional and named arguments, excluding
    self when a NULL is not present.
    
    CALL pops all arguments and the callable object off the stack,
    calls the callable object with those arguments, and pushes the return value
    returned by the callable object.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-CALL
    """
    OPCODE_NAME = 'CALL'
    OPCODE_VALUE = 171

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL) {
        #     PREDICTED(CALL);
        #     _PyCallCache *cache = (_PyCallCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         int is_meth = is_method(stack_pointer, oparg);
        #         int nargs = oparg + is_meth;
        #         PyObject *callable = PEEK(nargs + 1);
        #         next_instr--;
        #         _Py_Specialize_Call(callable, next_instr, nargs, kwnames);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(CALL, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     int total_args, is_meth;
        #     is_meth = is_method(stack_pointer, oparg);
        #     PyObject *function = PEEK(oparg + 1);
        #     if (!is_meth && Py_TYPE(function) == &PyMethod_Type) {
        #         PyObject *self = ((PyMethodObject *)function)->im_self;
        #         PEEK(oparg+1) = Py_NewRef(self);
        #         PyObject *meth = ((PyMethodObject *)function)->im_func;
        #         PEEK(oparg+2) = Py_NewRef(meth);
        #         Py_DECREF(function);
        #         is_meth = 1;
        #     }
        #     total_args = oparg + is_meth;
        #     function = PEEK(total_args + 1);
        #     int positional_args = total_args - KWNAMES_LEN();
        #     // Check if the call can be inlined or not
        #     if (Py_TYPE(function) == &PyFunction_Type &&
        #         tstate->interp->eval_frame == NULL &&
        #         ((PyFunctionObject *)function)->vectorcall == _PyFunction_Vectorcall)
        #     {
        #         int code_flags = ((PyCodeObject*)PyFunction_GET_CODE(function))->co_flags;
        #         PyObject *locals = code_flags & CO_OPTIMIZED ? NULL : Py_NewRef(PyFunction_GET_GLOBALS(function));
        #         STACK_SHRINK(total_args);
        #         _PyInterpreterFrame *new_frame = _PyEvalFramePushAndInit(
        #             tstate, (PyFunctionObject *)function, locals,
        #             stack_pointer, positional_args, kwnames
        #         );
        #         kwnames = NULL;
        #         STACK_SHRINK(2-is_meth);
        #         // The frame has stolen all the arguments from the stack,
        #         // so there is no need to clean them up.
        #         if (new_frame == NULL) {
        #             goto error;
        #         }
        #         JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #         DISPATCH_INLINED(new_frame);
        #     }
        #     /* Callable is not a normal Python function */
        #     PyObject *res;
        #     if (cframe.use_tracing) {
        #         res = trace_call_function(
        #             tstate, function, stack_pointer-total_args,
        #             positional_args, kwnames);
        #     }
        #     else {
        #         res = PyObject_Vectorcall(
        #             function, stack_pointer-total_args,
        #             positional_args | PY_VECTORCALL_ARGUMENTS_OFFSET,
        #             kwnames);
        #     }
        #     kwnames = NULL;
        #     assert((res != NULL) ^ (_PyErr_Occurred(tstate) != NULL));
        #     Py_DECREF(function);
        #     /* Clear the stack */
        #     STACK_SHRINK(total_args);
        #     for (int i = 0; i < total_args; i++) {
        #         Py_DECREF(stack_pointer[i]);
        #     }
        #     STACK_SHRINK(2-is_meth);
        #     PUSH(res);
        #     if (res == NULL) {
        #         goto error;
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_CALL);
        #     CHECK_EVAL_BREAKER();
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
