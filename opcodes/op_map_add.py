# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpMapAdd(BaseOpCode):
    """
    Calls dict.__setitem__(TOS1[-i], TOS1, TOS).  Used to implement dict
    comprehensions.
    
    New in version 3.1.
    
    Changed in version 3.8: Map value is TOS and map key is TOS1. Before, those were reversed.

    https://docs.python.org/3.12/library/dis.html#opcode-MAP_ADD
    """
    OPCODE_NAME = 'MAP_ADD'
    OPCODE_VALUE = 147

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(MAP_ADD) {
        #     PyObject *value = TOP();
        #     PyObject *key = SECOND();
        #     PyObject *map;
        #     STACK_SHRINK(2);
        #     map = PEEK(oparg);                      /* dict */
        #     assert(PyDict_CheckExact(map));
        #     /* map[key] = value */
        #     if (_PyDict_SetItem_Take2((PyDictObject *)map, key, value) != 0) {
        #         goto error;
        #     }
        #     PREDICT(JUMP_BACKWARD);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
