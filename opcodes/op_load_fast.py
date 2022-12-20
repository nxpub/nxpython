# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadFast(BaseOpCode):
    """
    Pushes a reference to the local co_varnames[var_num] onto the stack.
    
    Changed in version 3.12: This opcode is now only used in situations where the local variable is
    guaranteed to be initialized. It cannot raise UnboundLocalError.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_FAST
    """
    OPCODE_NAME = 'LOAD_FAST'
    OPCODE_VALUE = 124

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_FAST) {
        #     PyObject *value;
        #     value = GETLOCAL(oparg);
        #     assert(value != NULL);
        #     Py_INCREF(value);
        #     STACK_GROW(1);
        #     POKE(1, value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
