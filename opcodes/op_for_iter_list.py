# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpForIterList(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    name = 'FOR_ITER_LIST'
    value = 59

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- __0)
        # inst(FOR_ITER_LIST) {
        #     assert(cframe.use_tracing == 0);
        #     _PyListIterObject *it = (_PyListIterObject *)TOP();
        #     DEOPT_IF(Py_TYPE(it) != &PyListIter_Type, FOR_ITER);
        #     STAT_INC(FOR_ITER, hit);
        #     PyListObject *seq = it->it_seq;
        #     if (seq) {
        #         if (it->it_index < PyList_GET_SIZE(seq)) {
        #             PyObject *next = PyList_GET_ITEM(seq, it->it_index++);
        #             PUSH(Py_NewRef(next));
        #             JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER);
        #             goto end_for_iter_list;  // End of this instruction
        #         }
        #         it->it_seq = NULL;
        #         Py_DECREF(seq);
        #     }
        #     STACK_SHRINK(1);
        #     Py_DECREF(it);
        #     JUMPBY(INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1);
        # end_for_iter_list:
        # }
        # assert(cframe.use_tracing == 0)
        it = cls.stack.top()
        cls.flow.deopt_if(cls.api.Py_TYPE(it) != cls.api.PyListIter_Type, 'FOR_ITER')
        cls.flow.stat_inc('FOR_ITER', 'hit')
        seq = it.it_seq
        if seq:
            if it.it_index < cls.api.PyList_GET_SIZE(seq):
                next = cls.api.PyList_GET_ITEM(seq, it.it_index++)
                cls.stack.push(cls.api.Py_NewRef(next))
                cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER)
                goto end_for_iter_list  # End of this instruction
            it.it_seq = None
            cls.memory.dec_ref(seq)
        cls.stack.shrink(1)
        cls.memory.dec_ref(it)
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_FOR_ITER + oparg + 1)
                end_for_iter_list:
        cls.flow.dispatch()
