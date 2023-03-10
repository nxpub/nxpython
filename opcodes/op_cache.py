# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCache(OpCode):
    """
    Rather than being an actual instruction, this opcode is used to mark extra
    space for the interpreter to cache useful data directly in the bytecode
    itself. It is automatically hidden by all dis utilities, but can be
    viewed with show_caches=True.
    
    Logically, this space is part of the preceding instruction. Many opcodes
    expect to be followed by an exact number of caches, and will instruct the
    interpreter to skip over them at runtime.
    
    Populated caches can look like arbitrary instructions, so great care should
    be taken when reading or modifying raw, adaptive bytecode containing
    quickened data.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-CACHE
    """
    name = 'CACHE'
    value = 0

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- )
        # inst(CACHE) {
        #     Py_UNREACHABLE();
        # }
        raise NotImplementedError
