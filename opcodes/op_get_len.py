# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpGetLen(OpCode):
    """
    Push len(TOS) onto the stack.
    
    New in version 3.10.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_LEN
    """
    name = 'GET_LEN'
    value = 30

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(GET_LEN) {
        #     // PUSH(len(TOS))
        #     Py_ssize_t len_i = PyObject_Length(TOP());
        #     if (len_i < 0) {
        #         goto error;
        #     }
        #     PyObject *len_o = PyLong_FromSsize_t(len_i);
        #     if (len_o == NULL) {
        #         goto error;
        #     }
        #     PUSH(len_o);
        # }
        # cls.stack.push(len(TOS))
        len_i = cls.api.PyObject_Length(cls.stack.top())
        if len_i < 0:
            cls.flow.error()
        len_o = cls.api.PyLong_FromSsize_t(len_i)
        if len_o == None:
            cls.flow.error()
        cls.stack.push(len_o)
        cls.flow.dispatch()
