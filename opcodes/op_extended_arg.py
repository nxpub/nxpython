# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpExtendedArg(OpCode):
    """
    Prefixes any opcode which has an argument too big to fit into the default one
    byte. ext holds an additional byte which act as higher bits in the argument.
    For each opcode, at most three prefixal EXTENDED_ARG are allowed, forming
    an argument from two-byte to four-byte.

    https://docs.python.org/3.12/library/dis.html#opcode-EXTENDED_ARG
    """
    name = 'EXTENDED_ARG'
    value = 144

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: ( -- )
        # inst(EXTENDED_ARG) {
        #     assert(oparg);
        #     assert(cframe.use_tracing == 0);
        #     opcode = _Py_OPCODE(*next_instr);
        #     oparg = oparg << 8 | _Py_OPARG(*next_instr);
        #     PRE_DISPATCH_GOTO();
        #     DISPATCH_GOTO();
        # }
        # assert(oparg)
        # assert(cframe.use_tracing == 0)
        opcode = cls.api.private.Py_OPCODE(*next_instr)
        oparg = oparg << 8 | cls.api.private.Py_OPARG(*next_instr)
        PRE_DISPATCH_GOTO()
        DISPATCH_GOTO()
