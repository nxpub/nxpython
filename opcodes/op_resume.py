# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpResume(OpCode):
    """
    A no-op. Performs internal tracing, debugging and optimization checks.
    
    The where operand marks where the RESUME occurs:
    
    0 The start of a function
    
    1 After a yield expression
    
    2 After a yield from expression
    
    3 After an await expression
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-RESUME
    """
    name = 'RESUME'
    value = 151

    @classmethod
    def logic(cls, oparg: int) -> None:
        # inst(RESUME, (--)) {
        #     assert(tstate->cframe == &cframe);
        #     assert(frame == cframe.current_frame);
        #     if (_Py_atomic_load_relaxed_int32(eval_breaker) && oparg < 2) {
        #         goto handle_eval_breaker;
        #     }
        # }
        # assert(tstate->cframe == &cframe)
        # assert(frame == cframe.current_frame)
        if cls.api.private.Py_atomic_load_relaxed_int32(eval_breaker) and oparg < 2:
            cls.flow.handle_eval_breaker()
        cls.flow.dispatch()
