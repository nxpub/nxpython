# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpMatchMapping(OpCode):
    """
    If TOS is an instance of collections.abc.Mapping (or, more technically: if
    it has the Py_TPFLAGS_MAPPING flag set in its
    tp_flags), push True onto the stack.  Otherwise, push
    False.
    
    New in version 3.10.

    https://docs.python.org/3.12/library/dis.html#opcode-MATCH_MAPPING
    """
    name = 'MATCH_MAPPING'
    value = 31

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(MATCH_MAPPING) {
        #     PyObject *subject = TOP();
        #     int match = Py_TYPE(subject)->tp_flags & Py_TPFLAGS_MAPPING;
        #     PyObject *res = match ? Py_True : Py_False;
        #     PUSH(Py_NewRef(res));
        #     PREDICT(POP_JUMP_IF_FALSE);
        # }
        subject = cls.stack.top()
        match = cls.api.Py_TYPE(subject).tp_flags & cls.api.Py_TPFLAGS_MAPPING
        res = match ? cls.api.Py_True : cls.api.Py_False
        cls.stack.push(cls.api.Py_NewRef(res))
        cls.flow.dispatch()
