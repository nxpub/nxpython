# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpGetLen(BaseOpCode):
    """
    Push len(TOS) onto the stack.
    
    New in version 3.10.

    https://docs.python.org/3.12/library/dis.html#opcode-GET_LEN
    """
    OPCODE_NAME = 'GET_LEN'
    OPCODE_VALUE = 30

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(GET_LEN) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
