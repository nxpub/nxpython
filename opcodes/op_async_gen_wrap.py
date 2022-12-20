# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpAsyncGenWrap(BaseOpCode):
    """
    Wraps the value on top of the stack in an async_generator_wrapped_value.
    Used to yield in async generators.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-ASYNC_GEN_WRAP
    """
    OPCODE_NAME = 'ASYNC_GEN_WRAP'
    OPCODE_VALUE = 87

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(ASYNC_GEN_WRAP) {
        #     PyObject *v = TOP();
        #     assert(frame->f_code->co_flags & CO_ASYNC_GENERATOR);
        #     PyObject *w = _PyAsyncGenValueWrapperNew(v);
        #     if (w == NULL) {
        #         goto error;
        #     }
        #     SET_TOP(w);
        #     Py_DECREF(v);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
