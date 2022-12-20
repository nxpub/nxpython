# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpLoadClosure(BaseOpCode):
    """
    Pushes a reference to the cell contained in slot i of the “fast locals”
    storage.  The name of the variable is co_fastlocalnames[i].
    
    Note that LOAD_CLOSURE is effectively an alias for LOAD_FAST.
    It exists to keep bytecode a little more readable.
    
    Changed in version 3.11: i is no longer offset by the length of co_varnames.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_CLOSURE
    """
    OPCODE_NAME = 'LOAD_CLOSURE'
    OPCODE_VALUE = 136

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(LOAD_CLOSURE) {
        #     PyObject *value;
        #     /* We keep LOAD_CLOSURE so that the bytecode stays more readable. */
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
