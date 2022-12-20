# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c

from .base import BaseOpCode


class OpCompareOpFloatJump(BaseOpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'COMPARE_OP_FLOAT_JUMP'
    OPCODE_VALUE = 56

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(COMPARE_OP_FLOAT_JUMP) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     PyObject *_tmp_2 = PEEK(2);
        #     {
        #         PyObject *right = _tmp_1;
        #         PyObject *left = _tmp_2;
        #         size_t jump;
        #         uint16_t when_to_jump_mask = read_u16(&next_instr[1].cache);
        #                     assert(cframe.use_tracing == 0);
        #                     // Combined: COMPARE_OP (float ? float) + POP_JUMP_IF_(true/false)
        #                     DEOPT_IF(!PyFloat_CheckExact(left), COMPARE_OP);
        #                     DEOPT_IF(!PyFloat_CheckExact(right), COMPARE_OP);
        #                     STAT_INC(COMPARE_OP, hit);
        #                     double dleft = PyFloat_AS_DOUBLE(left);
        #                     double dright = PyFloat_AS_DOUBLE(right);
        #                     // 1 if NaN, 2 if <, 4 if >, 8 if ==; this matches when_to_jump_mask
        #                     int sign_ish = 1 << (2 * (dleft >= dright) + (dleft <= dright));
        #                     _Py_DECREF_SPECIALIZED(left, _PyFloat_ExactDealloc);
        #                     _Py_DECREF_SPECIALIZED(right, _PyFloat_ExactDealloc);
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
