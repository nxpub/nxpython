# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpStoreAttrSlot(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'STORE_ATTR_SLOT'
    OPCODE_VALUE = 158

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self, unused, type_version, index, value, owner) -> None:
        # TARGET(STORE_ATTR_SLOT) {
        #     PyObject *owner = PEEK(1);
        #     PyObject *value = PEEK(2);
        #     uint32_t type_version = read_u32(&next_instr[1].cache);
        #     uint16_t index = read_u16(&next_instr[3].cache);
        #     assert(cframe.use_tracing == 0);
        #     PyTypeObject *tp = Py_TYPE(owner);
        #     assert(type_version != 0);
        #     DEOPT_IF(tp->tp_version_tag != type_version, STORE_ATTR);
        #     char *addr = (char *)owner + index;
        #     STAT_INC(STORE_ATTR, hit);
        #     PyObject *old_value = *(PyObject **)addr;
        #     *(PyObject **)addr = value;
        #     Py_XDECREF(old_value);
        #     Py_DECREF(owner);
        #     STACK_SHRINK(2);
        #     JUMPBY(4);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
