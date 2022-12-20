# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMatchMapping(BaseOpCode):
    """
    If TOS is an instance of collections.abc.Mapping (or, more technically: if
    it has the Py_TPFLAGS_MAPPING flag set in its
    tp_flags), push True onto the stack.  Otherwise, push
    False.
    
    New in version 3.10.

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_MAPPING
    """
    OPCODE_NAME = 'MATCH_MAPPING'
    OPCODE_VALUE = 31

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MATCH_MAPPING) {
        #     PyObject *subject = TOP();
        #     int match = Py_TYPE(subject)->tp_flags & Py_TPFLAGS_MAPPING;
        #     PyObject *res = match ? Py_True : Py_False;
        #     PUSH(Py_NewRef(res));
        #     PREDICT(POP_JUMP_IF_FALSE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
