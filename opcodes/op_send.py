# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


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
    OPCODE_NAME = 'SEND'
    OPCODE_VALUE = 123

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(SEND) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
