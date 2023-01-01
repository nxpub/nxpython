# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpSend(OpCode):
    """
    Equivalent to TOS = TOS1.send(TOS). Used in yield from and await
    statements.
    
    If the call raises StopIteration, pop both items, push the
    exception’s value attribute, and increment the bytecode counter by
    delta.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-SEND
    """
    name = 'SEND'
    value = 123

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: SEND stack effect depends on jump flag
        # inst(SEND) {
        #     assert(frame != &entry_frame);
        #     assert(STACK_LEVEL() >= 2);
        #     PyObject *v = POP();
        #     PyObject *receiver = TOP();
        #     PySendResult gen_status;
        #     PyObject *retval;
        #     if (tstate->c_tracefunc == NULL) {
        #         gen_status = PyIter_Send(receiver, v, &retval);
        #     } else {
        #         if (Py_IsNone(v) && PyIter_Check(receiver)) {
        #             retval = Py_TYPE(receiver)->tp_iternext(receiver);
        #         }
        #         else {
        #             retval = PyObject_CallMethodOneArg(receiver, &_Py_ID(send), v);
        #         }
        #         if (retval == NULL) {
        #             if (tstate->c_tracefunc != NULL
        #                     && _PyErr_ExceptionMatches(tstate, PyExc_StopIteration))
        #                 call_exc_trace(tstate->c_tracefunc, tstate->c_traceobj, tstate, frame);
        #             if (_PyGen_FetchStopIterationValue(&retval) == 0) {
        #                 gen_status = PYGEN_RETURN;
        #             }
        #             else {
        #                 gen_status = PYGEN_ERROR;
        #             }
        #         }
        #         else {
        #             gen_status = PYGEN_NEXT;
        #         }
        #     }
        #     Py_DECREF(v);
        #     if (gen_status == PYGEN_ERROR) {
        #         assert(retval == NULL);
        #         goto error;
        #     }
        #     if (gen_status == PYGEN_RETURN) {
        #         assert(retval != NULL);
        #         Py_DECREF(receiver);
        #         SET_TOP(retval);
        #         JUMPBY(oparg);
        #     }
        #     else {
        #         assert(gen_status == PYGEN_NEXT);
        #         assert(retval != NULL);
        #         PUSH(retval);
        #     }
        # }
        # assert(frame != &entry_frame)
        # assert(STACK_LEVEL() >= 2)
        v = cls.stack.pop()
        receiver = cls.stack.top()
        if cls.frame.state.c_tracefunc == None:
            gen_status = cls.api.PyIter_Send(receiver, v, retval)
        else:
            if cls.api.Py_IsNone(v) and cls.api.PyIter_Check(receiver):
                retval = cls.api.Py_TYPE(receiver).tp_iternext(receiver)
            else:
                retval = cls.api.PyObject_CallMethodOneArg(receiver, cls.api.private.Py_ID('send'), v)
            if retval == None:
                if cls.frame.state.c_tracefunc != None
                        and cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_StopIteration))
                    call_exc_trace(cls.frame.state.c_tracefunc, cls.frame.state.c_traceobj, cls.frame.state, frame)
                if cls.api.private.PyGen_FetchStopIterationValue(retval) == 0:
                    gen_status = PYGEN_RETURN
                else:
                    gen_status = PYGEN_ERROR
            else:
                gen_status = PYGEN_NEXT
        cls.memory.dec_ref(v)
        if gen_status == PYGEN_ERROR:
            # assert(retval == NULL)
            cls.flow.error()
        if gen_status == PYGEN_RETURN:
            # assert(retval != NULL)
            cls.memory.dec_ref(receiver)
            cls.stack.set_top(retval)
            cls.flow.jump_by(oparg)
        else:
            # assert(gen_status == PYGEN_NEXT)
            # assert(retval != NULL)
            cls.stack.push(retval)
        cls.flow.dispatch()
