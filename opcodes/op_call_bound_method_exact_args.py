# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCallBoundMethodExactArgs(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'CALL_BOUND_METHOD_EXACT_ARGS'
    value = 24

    @classmethod
    def logic(cls) -> None:
        # // stack effect: (__0, __array[oparg] -- )
        # inst(CALL_BOUND_METHOD_EXACT_ARGS) {
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
        cls.flow.deopt_if(is_method(cls.stack, 'oparg'), CALL)
        function = cls.stack.peek(oparg + 1)
        cls.flow.deopt_if(cls.api.Py_TYPE(function) != cls.api.PyMethod_Type, 'CALL')
        cls.flow.stat_inc('CALL', 'hit')
        self = (function).im_self
        cls.stack.peek(oparg + 1) = cls.api.Py_NewRef(self)
        meth = (function).im_func
        cls.stack.peek(oparg + 2) = cls.api.Py_NewRef(meth)
        cls.memory.dec_ref(function)
        GO_TO_INSTRUCTION(CALL_PY_EXACT_ARGS)
