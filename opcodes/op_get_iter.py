# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpGetIter(OpCode):
    """
    Implements TOS = iter(TOS).

    https://docs.python.org/3.12/library/dis.html#opcode-GET_ITER
    """
    name = 'GET_ITER'
    value = 68

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- )
        # inst(GET_ITER) {
        #     /* before: [obj]; after [getiter(obj)] */
        #     PyObject *iterable = TOP();
        #     PyObject *iter = PyObject_GetIter(iterable);
        #     Py_DECREF(iterable);
        #     SET_TOP(iter);
        #     if (iter == NULL)
        #         goto error;
        # }
        # before: [obj] after [getiter(obj)] 
        iterable = cls.stack.top()
        iter = cls.api.PyObject_GetIter(iterable)
        cls.memory.dec_ref(iterable)
        cls.stack.set_top(iter)
        if iter == None:
            cls.flow.error()
        cls.flow.dispatch()
