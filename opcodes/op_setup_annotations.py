# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from opcodes import OpCode


class OpSetupAnnotations(OpCode):
    """
    Checks whether __annotations__ is defined in locals(), if not it is
    set up to an empty dict. This opcode is only emitted if a class
    or module body contains variable annotations
    statically.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-SETUP_ANNOTATIONS
    """
    name = 'SETUP_ANNOTATIONS'
    value = 85

    @classmethod
    def logic(cls) -> None:
        # inst(SETUP_ANNOTATIONS, (--)) {
        #     int err;
        #     PyObject *ann_dict;
        #     if (LOCALS() == NULL) {
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "no locals found when setting up annotations");
        #         ERROR_IF(true, error);
        #     }
        #     /* check if __annotations__ in locals()... */
        #     if (PyDict_CheckExact(LOCALS())) {
        #         ann_dict = _PyDict_GetItemWithError(LOCALS(),
        #                                             &_Py_ID(__annotations__));
        #         if (ann_dict == NULL) {
        #             ERROR_IF(_PyErr_Occurred(tstate), error);
        #             /* ...if not, create a new one */
        #             ann_dict = PyDict_New();
        #             ERROR_IF(ann_dict == NULL, error);
        #             err = PyDict_SetItem(LOCALS(), &_Py_ID(__annotations__),
        #                                  ann_dict);
        #             Py_DECREF(ann_dict);
        #             ERROR_IF(err, error);
        #         }
        #     }
        #     else {
        #         /* do the same if locals() is not a dict */
        #         ann_dict = PyObject_GetItem(LOCALS(), &_Py_ID(__annotations__));
        #         if (ann_dict == NULL) {
        #             ERROR_IF(!_PyErr_ExceptionMatches(tstate, PyExc_KeyError), error);
        #             _PyErr_Clear(tstate);
        #             ann_dict = PyDict_New();
        #             ERROR_IF(ann_dict == NULL, error);
        #             err = PyObject_SetItem(LOCALS(), &_Py_ID(__annotations__),
        #                                    ann_dict);
        #             Py_DECREF(ann_dict);
        #             ERROR_IF(err, error);
        #         }
        #         else {
        #             Py_DECREF(ann_dict);
        #         }
        #     }
        # }
        if cls.frame.get_locals() == None:
            cls.api.private.PyErr_Format(cls.frame.state, cls.api.PyExc_SystemError,
                          "no locals found when setting up annotations")
            cls.flow.error_if(True)
        # check if __annotations__ in locals()... 
        if cls.api.PyDict_CheckExact(cls.frame.get_locals()):
            ann_dict = cls.api.private.PyDict_GetItemWithError(cls.frame.get_locals(),
                                                cls.api.private.Py_ID('__annotations__'))
            if ann_dict == None:
                cls.flow.error_if(cls.api.private.PyErr_Occurred(cls.frame.state))
                # ...if not, create a new one 
                ann_dict = cls.api.PyDict_New()
                cls.flow.error_if(ann_dict == None)
                err = cls.api.PyDict_SetItem(cls.frame.get_locals(), cls.api.private.Py_ID('__annotations__'),
                                     ann_dict)
                cls.memory.dec_ref(ann_dict)
                cls.flow.error_if(err)
        else:
            # do the same if locals() is not a dict 
            ann_dict = cls.api.PyObject_GetItem(cls.frame.get_locals(), cls.api.private.Py_ID('__annotations__'))
            if ann_dict == None:
                cls.flow.error_if(not cls.api.private.PyErr_ExceptionMatches(cls.frame.state, cls.api.PyExc_KeyError))
                cls.api.private.PyErr_Clear(cls.frame.state)
                ann_dict = cls.api.PyDict_New()
                cls.flow.error_if(ann_dict == None)
                err = cls.api.PyObject_SetItem(cls.frame.get_locals(), cls.api.private.Py_ID('__annotations__'),
                                       ann_dict)
                cls.memory.dec_ref(ann_dict)
                cls.flow.error_if(err)
            else:
                cls.memory.dec_ref(ann_dict)
        cls.flow.dispatch()
