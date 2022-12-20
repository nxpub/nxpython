# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCheckEgMatch(BaseOpCode):
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
    OPCODE_NAME = 'CHECK_EG_MATCH'
    OPCODE_VALUE = 37

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(CHECK_EG_MATCH) {
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
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
