# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCallBoundMethodExactArgs(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'CALL_BOUND_METHOD_EXACT_ARGS'
    OPCODE_VALUE = 24

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CALL_BOUND_METHOD_EXACT_ARGS) {
        #     DEOPT_IF(is_method(stack_pointer, oparg), CALL);
        #     PyObject *function = PEEK(oparg + 1);
        #     DEOPT_IF(Py_TYPE(function) != &PyMethod_Type, CALL);
        #     STAT_INC(CALL, hit);
        #     PyObject *self = ((PyMethodObject *)function)->im_self;
        #     PEEK(oparg + 1) = Py_NewRef(self);
        #     PyObject *meth = ((PyMethodObject *)function)->im_func;
        #     PEEK(oparg + 2) = Py_NewRef(meth);
        #     Py_DECREF(function);
        #     GO_TO_INSTRUCTION(CALL_PY_EXACT_ARGS);
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
