# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpWithExceptStart(OpCode):
    """
    Calls the function in position 4 on the stack with arguments (type, val, tb)
    representing the exception at the top of the stack.
    Used to implement the call context_manager.__exit__(*exc_info()) when an exception
    has occurred in a with statement.
    
    New in version 3.9.
    
    Changed in version 3.11: The __exit__ function is in position 4 of the stack rather than 7.
    Exception representation on the stack now consist of one, not three, items.

    https://docs.python.org/3.12/library/dis.html#opcode-WITH_EXCEPT_START
    """
    OPCODE_NAME = 'WITH_EXCEPT_START'
    OPCODE_VALUE = 49

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, exit_func, lasti, unused, val) -> None:
        # TARGET(WITH_EXCEPT_START) {
        #     PyObject *val = PEEK(1);
        #     PyObject *lasti = PEEK(3);
        #     PyObject *exit_func = PEEK(4);
        #     PyObject *res;
        #     /* At the top of the stack are 4 values:
        #        - val: TOP = exc_info()
        #        - unused: SECOND = previous exception
        #        - lasti: THIRD = lasti of exception in exc_info()
        #        - exit_func: FOURTH = the context.__exit__ bound method
        #        We call FOURTH(type(TOP), TOP, GetTraceback(TOP)).
        #        Then we push the __exit__ return value.
        #     */
        #     PyObject *exc, *tb;

        #     assert(val && PyExceptionInstance_Check(val));
        #     exc = PyExceptionInstance_Class(val);
        #     tb = PyException_GetTraceback(val);
        #     Py_XDECREF(tb);
        #     assert(PyLong_Check(lasti));
        #     (void)lasti; // Shut up compiler warning if asserts are off
        #     PyObject *stack[4] = {NULL, exc, val, tb};
        #     res = PyObject_Vectorcall(exit_func, stack + 1,
        #             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        #     if (res == NULL) goto error;
        #     STACK_GROW(1);
        #     POKE(1, res);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
