# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadFastCheck(BaseOpCode):
    """
    Pushes a reference to the local co_varnames[var_num] onto the stack,
    raising an UnboundLocalError if the local variable has not been
    initialized.
    
    New in version 3.12.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_FAST_CHECK
    """
    OPCODE_NAME = 'LOAD_FAST_CHECK'
    OPCODE_VALUE = 127

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_FAST_CHECK) {
        #     PyObject *value;
        #     value = GETLOCAL(oparg);
        #     if (value == NULL) goto unbound_local_error;
        #     Py_INCREF(value);
        #     STACK_GROW(1);
        #     POKE(1, value);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
