# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpBuildMap(BaseOpCode):
    """
    Pushes a new dictionary object onto the stack.  Pops 2 * count items
    so that the dictionary holds count entries:
    {..., TOS3: TOS2, TOS1: TOS}.
    
    Changed in version 3.5: The dictionary is created from stack items instead of creating an
    empty dictionary pre-sized to hold count items.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_MAP
    """
    OPCODE_NAME = 'BUILD_MAP'
    OPCODE_VALUE = 105

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_MAP) {
        #     PyObject *map = _PyDict_FromItems(
        #             &PEEK(2*oparg), 2,
        #             &PEEK(2*oparg - 1), 2,
        #             oparg);
        #     if (map == NULL)
        #         goto error;

        #     while (oparg--) {
        #         Py_DECREF(POP());
        #         Py_DECREF(POP());
        #     }
        #     PUSH(map);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
