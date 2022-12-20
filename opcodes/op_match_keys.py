# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMatchKeys(BaseOpCode):
    """
    TOS is a tuple of mapping keys, and TOS1 is the match subject.  If TOS1
    contains all of the keys in TOS, push a tuple containing the
    corresponding values. Otherwise, push None.
    
    New in version 3.10.
    
    Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating
    success (True) or failure (False).

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_KEYS
    """
    OPCODE_NAME = 'MATCH_KEYS'
    OPCODE_VALUE = 33

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MATCH_KEYS) {
        #     // On successful match, PUSH(values). Otherwise, PUSH(None).
        #     PyObject *keys = TOP();
        #     PyObject *subject = SECOND();
        #     PyObject *values_or_none = match_keys(tstate, subject, keys);
        #     if (values_or_none == NULL) {
        #         goto error;
        #     }
        #     PUSH(values_or_none);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
