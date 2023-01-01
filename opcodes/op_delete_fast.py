# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteFast(OpCode):
    """
    Deletes local co_varnames[var_num].

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_FAST
    """
    name = 'DELETE_FAST'
    value = 126

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DELETE_FAST, (--)) {
        #     PyObject *v = GETLOCAL(oparg);
        #     ERROR_IF(v == NULL, unbound_local_error);
        #     SETLOCAL(oparg, NULL);
        # }
        v = cls.frame.get_local(oparg)
        cls.flow.unbound_local_error_if(v == None)
        SETLOCAL(oparg, None)
        cls.flow.dispatch()
