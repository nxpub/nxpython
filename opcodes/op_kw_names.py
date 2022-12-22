# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpKwNames(OpCode):
    """
    Prefixes CALL.
    Stores a reference to co_consts[consti] into an internal variable
    for use by CALL. co_consts[consti] must be a tuple of strings.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-KW_NAMES
    """
    OPCODE_NAME = 'KW_NAMES'
    OPCODE_VALUE = 172

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(KW_NAMES) {
        #     assert(kwnames == NULL);
        #     assert(oparg < PyTuple_GET_SIZE(consts));
        #     kwnames = GETITEM(consts, oparg);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
