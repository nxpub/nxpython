# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDeleteAttr(OpCode):
    """
    Implements del TOS.name, using namei as index into co_names.

    https://docs.python.org/3.12/library/dis.html#opcode-DELETE_ATTR
    """
    name = 'DELETE_ATTR'
    value = 96

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DELETE_ATTR, (owner --)) {
        #     PyObject *name = GETITEM(names, oparg);
        #     int err = PyObject_SetAttr(owner, name, (PyObject *)NULL);
        #     Py_DECREF(owner);
        #     ERROR_IF(err, error);
        # }
        owner = cls.stack.peek(1)
        name = cls.frame.get_name(oparg)
        err = cls.api.PyObject_SetAttr(owner, name, None)
        cls.memory.dec_ref(owner)
        cls.flow.error_if(err, 1)
        cls.stack.shrink(1)
        cls.flow.dispatch()
