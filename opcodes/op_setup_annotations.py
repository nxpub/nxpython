# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpSetupAnnotations(OpCode):
    """
    Checks whether __annotations__ is defined in locals(), if not it is
    set up to an empty dict. This opcode is only emitted if a class
    or module body contains variable annotations
    statically.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-SETUP_ANNOTATIONS
    """
    OPCODE_NAME = 'SETUP_ANNOTATIONS'
    OPCODE_VALUE = 85

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(SETUP_ANNOTATIONS) {
        #     int err;
        #     PyObject *ann_dict;
        #     if (LOCALS() == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals found when setting up annotations");
        #         goto error;
        #     }
        #     /* check if __annotations__ in locals()... */
        #     if (PyDict_CheckExact(LOCALS())) {
        #         ann_dict = _PyDict_GetItemWithError(LOCALS(),
        #                                             &_Py_ID(__annotations__));
        #         if (ann_dict == NULL) {
        #             if (_PyErr_Occurred(tstate)) {
        #                 goto error;
        #             }
        #             /* ...if not, create a new one */
        #             ann_dict = PyDict_New();
        #             if (ann_dict == NULL) {
        #                 goto error;
        #             }
        #             err = PyDict_SetItem(LOCALS(), &_Py_ID(__annotations__),
        #                                  ann_dict);
        #             Py_DECREF(ann_dict);
        #             if (err != 0) {
        #                 goto error;
        #             }
        #         }
        #     }
        #     else {
        #         /* do the same if locals() is not a dict */
        #         ann_dict = PyObject_GetItem(LOCALS(), &_Py_ID(__annotations__));
        #         if (ann_dict == NULL) {
        #             if (!_PyErr_ExceptionMatches(tstate, PyExc_KeyError)) {
        #                 goto error;
        #             }
        #             _PyErr_Clear(tstate);
        #             ann_dict = PyDict_New();
        #             if (ann_dict == NULL) {
        #                 goto error;
        #             }
        #             err = PyObject_SetItem(LOCALS(), &_Py_ID(__annotations__),
        #                                    ann_dict);
        #             Py_DECREF(ann_dict);
        #             if (err != 0) {
        #                 goto error;
        #             }
        #         }
        #         else {
        #             Py_DECREF(ann_dict);
        #         }
        #     }
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
