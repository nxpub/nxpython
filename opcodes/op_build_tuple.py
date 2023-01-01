# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpBuildTuple(OpCode):
    """
    Creates a tuple consuming count items from the stack, and pushes the
    resulting tuple onto the stack.

    https://docs.python.org/3.12/library/dis.html#opcode-BUILD_TUPLE
    """
    name = 'BUILD_TUPLE'
    value = 102

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // stack effect: (__array[oparg] -- __0)
        # inst(BUILD_TUPLE) {
        #     STACK_SHRINK(oparg);
        #     PyObject *tup = _PyTuple_FromArraySteal(stack_pointer, oparg);
        #     if (tup == NULL)
        #         goto error;
        #     PUSH(tup);
        # }
        cls.stack.shrink(oparg)
        tup = cls.api.private.PyTuple_FromArraySteal(cls.stack, oparg)
        if tup == None:
            cls.flow.error()
        cls.stack.push(tup)
        cls.flow.dispatch()
