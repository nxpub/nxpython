# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpImportFrom(OpCode):
    """
    Loads the attribute co_names[namei] from the module found in TOS. The
    resulting object is pushed onto the stack, to be subsequently stored by a
    STORE_FAST instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_FROM
    """
    name = 'IMPORT_FROM'
    value = 109

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(IMPORT_FROM, (from -- from, res)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     res = import_from(tstate, from, name);
        #     ERROR_IF(res == NULL, error);
        # }
        from = cls.stack.peek(1)
        name = cls.frame.get_name(oparg)
        res = import_from(cls.frame.state, from, name)
        cls.flow.error_if(res == None)
        cls.stack.grow(1)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
