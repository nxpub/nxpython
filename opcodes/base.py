from abc import ABCMeta, abstractmethod


class BaseOpCode(metaclass=ABCMeta):

    OPCODE_NAME = None
    OPCODE_VALUE = None

    def __init__(self):
        pass

    @abstractmethod
    def extract(self, stack):
        raise NotImplementedError

    @abstractmethod
    def transform(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def load(self, stack):
        raise NotImplementedError
