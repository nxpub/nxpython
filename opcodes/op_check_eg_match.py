# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpCheckEgMatch(OpCode):
    """
    Performs exception matching for except*. Applies split(TOS) on
    the exception group representing TOS1.
    
    In case of a match, pops two items from the stack and pushes the
    non-matching subgroup (None in case of full match) followed by the
    matching subgroup. When there is no match, pops one item (the match
    type) and pushes None.
    
    New in version 3.11.

    https://docs.python.org/3.12/library/dis.html#opcode-CHECK_EG_MATCH
    """
    name = 'CHECK_EG_MATCH'
    value = 37

    @classmethod
    def logic(cls) -> None:
        # // stack effect: ( -- )
        # inst(CHECK_EG_MATCH) {
        #     PyObject *match_type = POP();
        #     if (check_except_star_type_valid(tstate, match_type) < 0) {
        #         Py_DECREF(match_type);
        #         goto error;
        #     }

        #     PyObject *exc_value = TOP();
        #     PyObject *match = NULL, *rest = NULL;
        #     int res = exception_group_match(exc_value, match_type,
        #                                     &match, &rest);
        #     Py_DECREF(match_type);
        #     if (res < 0) {
        #         goto error;
        #     }

        #     if (match == NULL || rest == NULL) {
        #         assert(match == NULL);
        #         assert(rest == NULL);
        #         goto error;
        #     }
        #     if (Py_IsNone(match)) {
        #         PUSH(match);
        #         Py_XDECREF(rest);
        #     }
        #     else {
        #         /* Total or partial match - update the stack from
        #          * [val]
        #          * to
        #          * [rest, match]
        #          * (rest can be Py_None)
        #          */

        #         SET_TOP(rest);
        #         PUSH(match);
        #         PyErr_SetExcInfo(NULL, Py_NewRef(match), NULL);
        #         Py_DECREF(exc_value);
        #     }
        # }
        match_type = cls.stack.pop()
        if check_except_star_type_valid(cls.frame.state, match_type) < 0:
            cls.memory.dec_ref(match_type)
            cls.flow.error()

        exc_value = cls.stack.top()
        match = None, *rest = None
        res = exception_group_match(exc_value, match_type,
                                        match, rest)
        cls.memory.dec_ref(match_type)
        if res < 0:
            cls.flow.error()

        if match == None or rest == None:
            # assert(match == NULL)
            # assert(rest == NULL)
            cls.flow.error()
        if cls.api.Py_IsNone(match):
            cls.stack.push(match)
            cls.memory.dec_ref_x(rest)
        else:
            # Total or partial match - update the stack from
        #      * [val]
        #      * to
        #      * [rest, match]
        #      * (rest can be Py_None)
        #      

            cls.stack.set_top(rest)
            cls.stack.push(match)
            cls.api.PyErr_SetExcInfo(None, cls.api.Py_NewRef(match), None)
            cls.memory.dec_ref(exc_value)
        cls.flow.dispatch()
