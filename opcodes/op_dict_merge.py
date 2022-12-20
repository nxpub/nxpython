# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpDictMerge(BaseOpCode):
    """
    Like DICT_UPDATE but raises an exception for duplicate keys.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-DICT_MERGE
    """
    OPCODE_NAME = 'DICT_MERGE'
    OPCODE_VALUE = 164

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(DICT_MERGE) {
        #     PyObject *update = POP();
        #     PyObject *dict = PEEK(oparg);

        #     if (_PyDict_MergeEx(dict, update, 2) < 0) {
        #         format_kwargs_error(tstate, PEEK(2 + oparg), update);
        #         Py_DECREF(update);
        #         goto error;
        #     }
        #     Py_DECREF(update);
        #     PREDICT(CALL_FUNCTION_EX);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
