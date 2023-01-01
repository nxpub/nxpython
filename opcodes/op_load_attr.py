# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpLoadAttr(OpCode):
    """
    If the low bit of namei is not set, this replaces TOS with
    getattr(TOS, co_names[namei>>1]).
    
    If the low bit of namei is set, this will attempt to load a method named
    co_names[namei>>1] from the TOS object. TOS is popped.
    This bytecode distinguishes two cases: if TOS has a method with the correct
    name, the bytecode pushes the unbound method and TOS. TOS will be used as
    the first argument (self) by CALL when calling the
    unbound method. Otherwise, NULL and the object return by the attribute
    lookup are pushed.
    
    Changed in version 3.12: If the low bit of namei is set, then a NULL or self is
    pushed to the stack before the attribute or unbound method respectively.

    https://docs.python.org/3.12/library/dis.html#opcode-LOAD_ATTR
    """
    name = 'LOAD_ATTR'
    value = 106

    @classmethod
    def logic(cls, oparg: int) -> None:
        # // error: LOAD_ATTR has irregular stack effect
        # inst(LOAD_ATTR) {
        #     _PyAttrCache *cache = (_PyAttrCache *)next_instr;
        #     if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {
        #         assert(cframe.use_tracing == 0);
        #         PyObject *owner = TOP();
        #         PyObject *name = GETITEM(names, oparg>>1);
        #         next_instr--;
        #         _Py_Specialize_LoadAttr(owner, next_instr, name);
        #         DISPATCH_SAME_OPARG();
        #     }
        #     STAT_INC(LOAD_ATTR, deferred);
        #     DECREMENT_ADAPTIVE_COUNTER(cache->counter);
        #     PyObject *name = GETITEM(names, oparg >> 1);
        #     PyObject *owner = TOP();
        #     if (oparg & 1) {
        #         /* Designed to work in tandem with CALL. */
        #         PyObject* meth = NULL;

        #         int meth_found = _PyObject_GetMethod(owner, name, &meth);

        #         if (meth == NULL) {
        #             /* Most likely attribute wasn't found. */
        #             goto error;
        #         }

        #         if (meth_found) {
        #             /* We can bypass temporary bound method object.
        #                meth is unbound method and obj is self.

        #                meth | self | arg1 | ... | argN
        #              */
        #             SET_TOP(meth);
        #             PUSH(owner);  // self
        #         }
        #         else {
        #             /* meth is not an unbound method (but a regular attr, or
        #                something was returned by a descriptor protocol).  Set
        #                the second element of the stack to NULL, to signal
        #                CALL that it's not a method call.

        #                NULL | meth | arg1 | ... | argN
        #             */
        #             SET_TOP(NULL);
        #             Py_DECREF(owner);
        #             PUSH(meth);
        #         }
        #     }
        #     else {
        #         PyObject *res = PyObject_GetAttr(owner, name);
        #         if (res == NULL) {
        #             goto error;
        #         }
        #         Py_DECREF(owner);
        #         SET_TOP(res);
        #     }
        #     JUMPBY(INLINE_CACHE_ENTRIES_LOAD_ATTR);
        # }
        name = cls.frame.get_name(oparg >> 1)
        owner = cls.stack.top()
        if oparg & 1:
            # Designed to work in tandem with CALL. 
            cls.api.PyObject* meth = None

            meth_found = cls.api.private.PyObject_GetMethod(owner, name, meth)

            if meth == None:
                # Most likely attribute wasn't found. 
                cls.flow.error()

            if meth_found:
                # We can bypass temporary bound method object.
        #            meth is unbound method and obj is self.

        #            meth | self | arg1 | ... | argN
        #          
                cls.stack.set_top(meth)
                cls.stack.push(owner)  # self
            else:
                # meth is not an unbound method (but a regular attr, or
        #            something was returned by a descriptor protocol).  Set
        #            the second element of the stack to NULL, to signal
        #            CALL that it's not a method call.

        #            NULL | meth | arg1 | ... | argN
        #         
                cls.stack.set_top(None)
                cls.memory.dec_ref(owner)
                cls.stack.push(meth)
        else:
            res = cls.api.PyObject_GetAttr(owner, name)
            if res == None:
                cls.flow.error()
            cls.memory.dec_ref(owner)
            cls.stack.set_top(res)
        cls.flow.skip(cls.api.internal.INLINE_CACHE_ENTRIES_LOAD_ATTR)
        cls.flow.dispatch()
