# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpDictMerge(OpCode):
    """
    Like DICT_UPDATE but raises an exception for duplicate keys.
    
    New in version 3.9.

    https://docs.python.org/3.12/library/dis.html#opcode-DICT_MERGE
    """
    name = 'DICT_MERGE'
    value = 164

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(DICT_MERGE, (update --)) {
        #     PyObject *dict = PEEK(oparg + 1);  // update is still on the stack

        #     if (_PyDict_MergeEx(dict, update, 2) < 0) {
        #         format_kwargs_error(tstate, PEEK(3 + oparg), update);
        #         DECREF_INPUTS();
        #         ERROR_IF(true, error);
        #     }
        #     DECREF_INPUTS();
        #     PREDICT(CALL_FUNCTION_EX);
        # }
        update = cls.stack.peek(1)
        dict = cls.stack.peek(oparg + 1)  # update is still on the stack

        if cls.api.private.PyDict_MergeEx(dict, update, 2) < 0:
            format_kwargs_error(cls.frame.state, cls.stack.peek(3 + oparg), update)
            cls.memory.dec_ref(update)
            cls.flow.error_if(True, 1)
        cls.memory.dec_ref(update)
        cls.stack.shrink(1)
        cls.flow.dispatch()
