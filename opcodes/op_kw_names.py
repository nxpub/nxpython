# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpKwNames(OpCode):
    """
    Prefixes CALL.
    Stores a reference to co_consts[consti] into an internal variable
    for use by CALL. co_consts[consti] must be a tuple of strings.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-KW_NAMES
    """
    name = 'KW_NAMES'
    value = 172

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: ( -- )
        # inst(KW_NAMES) {
        #     assert(kwnames == NULL);
        #     assert(oparg < PyTuple_GET_SIZE(consts));
        #     kwnames = GETITEM(consts, oparg);
        # }
        # assert(kwnames == NULL)
        # assert(oparg < PyTuple_GET_SIZE(consts))
        kwnames = cls.frame.get_const(oparg)
        cls.flow.dispatch()
