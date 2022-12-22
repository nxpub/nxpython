from abc import ABCMeta, abstractmethod


class OpCode(metaclass=ABCMeta):

    OPCODE_NAME = None
    OPCODE_VALUE = None

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def extract(cls, stack):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def transform(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def load(cls, stack):
        raise NotImplementedError
