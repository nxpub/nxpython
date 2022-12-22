# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpMatchSequence(OpCode):
    """
    If TOS is an instance of collections.abc.Sequence and is not an instance
    of str/bytes/bytearray (or, more technically: if it has
    the Py_TPFLAGS_SEQUENCE flag set in its tp_flags),
    push True onto the stack.  Otherwise, push False.
    
    New in version 3.10.

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_SEQUENCE
    """
    OPCODE_NAME = 'MATCH_SEQUENCE'
    OPCODE_VALUE = 32

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MATCH_SEQUENCE) {
        #     PyObject *subject = TOP();
        #     int match = Py_TYPE(subject)->tp_flags & Py_TPFLAGS_SEQUENCE;
        #     PyObject *res = match ? Py_True : Py_False;
        #     PUSH(Py_NewRef(res));
        #     PREDICT(POP_JUMP_IF_FALSE);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
