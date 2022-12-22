# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpBuildTuple(OpCode):
    """
    Creates a tuple consuming count items from the stack, and pushes the
    resulting tuple onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_TUPLE
    """
    OPCODE_NAME = 'BUILD_TUPLE'
    OPCODE_VALUE = 102

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(BUILD_TUPLE) {
        #     STACK_SHRINK(oparg);
        #     PyObject *tup = _PyTuple_FromArraySteal(stack_pointer, oparg);
        #     if (tup == NULL)
        #         goto error;
        #     PUSH(tup);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
