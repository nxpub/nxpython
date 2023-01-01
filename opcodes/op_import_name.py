# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpImportName(OpCode):
    """
    Imports the module co_names[namei].  TOS and TOS1 are popped and provide
    the fromlist and level arguments of __import__().  The module
    object is pushed onto the stack.  The current namespace is not affected: for
    a proper import statement, a subsequent STORE_FAST instruction
    modifies the namespace.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_NAME
    """
    name = 'IMPORT_NAME'
    value = 108

    @classmethod
    def logic(cls, oparg: int) -> None:
        #  inst(IMPORT_NAME, (level, fromlist -- res)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     res = import_name(tstate, frame, name, fromlist, level);
        #     DECREF_INPUTS();
        #     ERROR_IF(res == NULL, error);
        # }
        fromlist = cls.stack.peek(1)
        level = cls.stack.peek(2)
        name = cls.frame.get_name(oparg)
        res = import_name(cls.frame.state, frame, name, fromlist, level)
        cls.memory.dec_ref(level)
        cls.memory.dec_ref(fromlist)
        cls.flow.error_if(res == None, 2)
        cls.stack.shrink(1)
        cls.stack.poke(1, res)
        cls.flow.dispatch()
