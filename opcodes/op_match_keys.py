# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpMatchKeys(OpCode):
    """
    TOS is a tuple of mapping keys, and TOS1 is the match subject.  If TOS1
    contains all of the keys in TOS, push a tuple containing the
    corresponding values. Otherwise, push None.
    
    New in version 3.10.
    
    Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating
    success (True) or failure (False).

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_KEYS
    """
    name = 'MATCH_KEYS'
    value = 33

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(MATCH_KEYS) {
        #     // On successful match, PUSH(values). Otherwise, PUSH(None).
        #     PyObject *keys = TOP();
        #     PyObject *subject = SECOND();
        #     PyObject *values_or_none = match_keys(tstate, subject, keys);
        #     if (values_or_none == NULL) {
        #         goto error;
        #     }
        #     PUSH(values_or_none);
        # }
        # On successful match, cls.stack.push(values). Otherwise, cls.stack.push(None).
        keys = cls.stack.top()
        subject = cls.stack.second()
        values_or_none = match_keys(cls.frame.state, subject, keys)
        if values_or_none == None:
            cls.flow.error()
        cls.stack.push(values_or_none)
        cls.flow.dispatch()
