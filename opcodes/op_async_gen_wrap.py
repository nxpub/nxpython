# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpAsyncGenWrap(OpCode):
    """
    Wraps the value on top of the stack in an async_generator_wrapped_value.
    Used to yield in async generators.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-ASYNC_GEN_WRAP
    """
    name = 'ASYNC_GEN_WRAP'
    value = 87

    @classmethod
    def logic(cls) -> None:
        # inst(ASYNC_GEN_WRAP, (v -- w)) {
        #     assert(frame->f_code->co_flags & CO_ASYNC_GENERATOR);
        #     w = _PyAsyncGenValueWrapperNew(v);
        #     DECREF_INPUTS();
        #     ERROR_IF(w == NULL, error);
        # }
        v = cls.stack.peek(1)
        # assert(frame->f_code->co_flags & CO_ASYNC_GENERATOR)
        w = cls.api.private.PyAsyncGenValueWrapperNew(v)
        cls.memory.dec_ref(v)
        cls.flow.error_if(w == None, 1)
        cls.stack.poke(1, w)
        cls.flow.dispatch()
