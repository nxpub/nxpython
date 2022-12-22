# Auto-generated via https://github.com/python/cpython/blob/main/Python/bytecodes.c
from .base import OpCode


class OpFormatValue(OpCode):
    """
    Used for implementing formatted literal strings (f-strings).  Pops
    an optional fmt_spec from the stack, then a required value.
    flags is interpreted as follows:
    
    (flags & 0x03) == 0x00: value is formatted as-is.
    
    (flags & 0x03) == 0x01: call str() on value before
    formatting it.
    
    (flags & 0x03) == 0x02: call repr() on value before
    formatting it.
    
    (flags & 0x03) == 0x03: call ascii() on value before
    formatting it.
    
    (flags & 0x04) == 0x04: pop fmt_spec from the stack and use
    it, else use an empty fmt_spec.
    
    Formatting is performed using PyObject_Format().  The
    result is pushed on the stack.
    
    New in version 3.6.

    https://docs.python.org/3.12/library/dis.html#opcode-FORMAT_VALUE
    """
    OPCODE_NAME = 'FORMAT_VALUE'
    OPCODE_VALUE = 155

    def extract(self, stack) -> None:
        raise NotImplementedError

    def transform(self) -> None:
        # TARGET(FORMAT_VALUE) {
        #     /* Handles f-string value formatting. */
        #     PyObject *result;
        #     PyObject *fmt_spec;
        #     PyObject *value;
        #     PyObject *(*conv_fn)(PyObject *);
        #     int which_conversion = oparg & FVC_MASK;
        #     int have_fmt_spec = (oparg & FVS_MASK) == FVS_HAVE_SPEC;

        #     fmt_spec = have_fmt_spec ? POP() : NULL;
        #     value = POP();

        #     /* See if any conversion is specified. */
        #     switch (which_conversion) {
        #     case FVC_NONE:  conv_fn = NULL;           break;
        #     case FVC_STR:   conv_fn = PyObject_Str;   break;
        #     case FVC_REPR:  conv_fn = PyObject_Repr;  break;
        #     case FVC_ASCII: conv_fn = PyObject_ASCII; break;
        #     default:
        #         _PyErr_Format(tstate, PyExc_SystemError,
        #                       "unexpected conversion flag %d",
        #                       which_conversion);
        #         goto error;
        #     }

        #     /* If there's a conversion function, call it and replace
        #        value with that result. Otherwise, just use value,
        #        without conversion. */
        #     if (conv_fn != NULL) {
        #         result = conv_fn(value);
        #         Py_DECREF(value);
        #         if (result == NULL) {
        #             Py_XDECREF(fmt_spec);
        #             goto error;
        #         }
        #         value = result;
        #     }

        #     /* If value is a unicode object, and there's no fmt_spec,
        #        then we know the result of format(value) is value
        #        itself. In that case, skip calling format(). I plan to
        #        move this optimization in to PyObject_Format()
        #        itself. */
        #     if (PyUnicode_CheckExact(value) && fmt_spec == NULL) {
        #         /* Do nothing, just transfer ownership to result. */
        #         result = value;
        #     } else {
        #         /* Actually call format(). */
        #         result = PyObject_Format(value, fmt_spec);
        #         Py_DECREF(value);
        #         Py_XDECREF(fmt_spec);
        #         if (result == NULL) {
        #             goto error;
        #         }
        #     }

        #     PUSH(result);
        #     DISPATCH();
        # }
        raise NotImplementedError

    def load(self, stack) -> None:
        raise NotImplementedError
