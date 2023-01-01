from abc import ABCMeta
from contextlib import contextmanager
from typing import Tuple, Optional, Any

from python import Stack, Api


class OpCode(metaclass=ABCMeta):

    __registry__ = {}
    name = value = None

    stack: Stack = None
    api: Api = None
    flow: Any = None
    memory: Any = None
    frame: Any = None

    def __class_getitem__(cls, item):
        return cls.__registry__[item]

    def __init_subclass__(cls, **kwargs):
        OpCode.__registry__[cls.name] = OpCode.__registry__[cls.value] = cls

    def __new__(cls, *args, **kwargs):
        return cls.logic(*args, **kwargs)

    @classmethod
    def logic(cls, *args, **kwargs):
        raise NotImplementedError


class Instruction:

    __slots__ = ['_oparg', '_opcode']

    def __init__(self, opcode: int, oparg: Optional[int] = None):
        self._oparg = oparg
        self._opcode = OpCode[opcode]

    def __call__(self, *args, **kwargs):
        self._opcode.logic(*args, **kwargs, oparg=self._oparg)


@contextmanager
def environment(stack: Stack, api: Api):
    assert (OpCode.stack is None) and (OpCode.api is None)
    OpCode.stack = stack
    OpCode.api = api
    yield
    OpCode.stack = None
    OpCode.api = None
