# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpImportFrom(BaseOpCode):
    """
    Loads the attribute co_names[namei] from the module found in TOS. The
    resulting object is pushed onto the stack, to be subsequently stored by a
    STORE_FAST instruction.

    https://docs.python.org/3.12/library/dis.html#opcode-IMPORT_FROM
    """
    OPCODE_NAME = 'IMPORT_FROM'
    OPCODE_VALUE = 109

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(IMPORT_FROM) {
        #     PyObject *name = GETITEM(names, oparg);
        #     PyObject *from = TOP();
        #     PyObject *res;
        #     res = import_from(tstate, from, name);
        #     PUSH(res);
        #     if (res == NULL)
        #         goto error;
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
