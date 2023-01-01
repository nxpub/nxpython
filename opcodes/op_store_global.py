# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpStoreGlobal(OpCode):
    """
    Works as STORE_NAME, but stores the name as a global.

    https://docs.python.org/3.12/library/dis.html#opcode-STORE_GLOBAL
    """
    name = 'STORE_GLOBAL'
    value = 97

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(STORE_GLOBAL, (v --)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyDict_SetItem(GLOBALS(), name, v);
        #     Py_DECREF(v);
        #     ERROR_IF(err, error);
        # }
        v = cls.stack.peek(1)
        name = cls.frame.get_name(oparg)
        err = cls.api.PyDict_SetItem(cls.frame.get_globals(), name, v)
        cls.memory.dec_ref(v)
        cls.flow.error_if(err, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
