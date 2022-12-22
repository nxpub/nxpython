# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpCompareOpStrJump(OpCode):
    """
    TODO: Cannot find documentation via dis docs!
    """
    OPCODE_NAME = 'COMPARE_OP_STR_JUMP'
    OPCODE_VALUE = 58

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(COMPARE_OP_STR_JUMP) {
        #     PyObject *_tmp_1 = PEEK(1);
        #     PyObject *_tmp_2 = PEEK(2);
        #     {
        #         PyObject *right = _tmp_1;
        #         PyObject *left = _tmp_2;
        #         size_t jump;
        #         uint16_t invert = read_u16(&next_instr[1].cache);
        #                     assert(cframe.use_tracing == 0);
        #                     // Combined: COMPARE_OP (str == str or str != str) + POP_JUMP_IF_(true/false)
        #                     DEOPT_IF(!PyUnicode_CheckExact(left), COMPARE_OP);
        #                     DEOPT_IF(!PyUnicode_CheckExact(right), COMPARE_OP);
        #                     STAT_INC(COMPARE_OP, hit);
        #                     int res = _PyUnicode_Equal(left, right);
        #                     assert(oparg == Py_EQ || oparg == Py_NE);
        #                     _Py_DECREF_SPECIALIZED(left, _PyUnicode_ExactDealloc);
        #                     _Py_DECREF_SPECIALIZED(right, _PyUnicode_ExactDealloc);
        #                     assert(res == 0 || res == 1);
        #                     assert(invert == 0 || invert == 1);
        #                     jump = res ^ invert;
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
