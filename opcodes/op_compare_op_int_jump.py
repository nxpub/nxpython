# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCompareOpIntJump(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'COMPARE_OP_INT_JUMP'
    OPCODE_VALUE = 57

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(COMPARE_OP_INT_JUMP) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     PyObject *_tmp_2 = PEEK(2);
        #     {
        #         PyObject *right = _tmp_1;
        #         PyObject *left = _tmp_2;
        #         size_t jump;
        #         uint16_t when_to_jump_mask = read_u16(&next_instr[1].cache);
        #                     assert(cframe.use_tracing == 0);
        #                     // Combined: COMPARE_OP (int ? int) + POP_JUMP_IF_(true/false)
        #                     DEOPT_IF(!PyLong_CheckExact(left), COMPARE_OP);
        #                     DEOPT_IF(!PyLong_CheckExact(right), COMPARE_OP);
        #                     DEOPT_IF((size_t)(Py_SIZE(left) + 1) > 2, COMPARE_OP);
        #                     DEOPT_IF((size_t)(Py_SIZE(right) + 1) > 2, COMPARE_OP);
        #                     STAT_INC(COMPARE_OP, hit);
        #                     assert(Py_ABS(Py_SIZE(left)) <= 1 && Py_ABS(Py_SIZE(right)) <= 1);
        #                     Py_ssize_t ileft = Py_SIZE(left) * ((PyLongObject *)left)->ob_digit[0];
        #                     Py_ssize_t iright = Py_SIZE(right) * ((PyLongObject *)right)->ob_digit[0];
        #                     // 2 if <, 4 if >, 8 if ==; this matches when_to_jump_mask
        #                     int sign_ish = 1 << (2 * (ileft >= iright) + (ileft <= iright));
        #                     _Py_DECREF_SPECIALIZED(left, (destructor)PyObject_Free);
        #                     _Py_DECREF_SPECIALIZED(right, (destructor)PyObject_Free);
        #                     jump = sign_ish & when_to_jump_mask;
        #         _tmp_2 = (PyObject *)jump;
        #     }
        #     JUMPBY(2);
        #     NEXTOPARG();
        #     JUMPBY(1);
        #     {
        #         size_t jump = (size_t)_tmp_2;
        #                     assert(opcode == POP_JUMP_IF_FALSE || opcode == POP_JUMP_IF_TRUE);
        #                     if (jump) {
        #                         JUMPBY(oparg);
        #                     }
        #     }
        #     STACK_SHRINK(2);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
