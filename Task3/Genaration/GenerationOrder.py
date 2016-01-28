from abc import ABCMeta, abstractmethod


class GenerationOrder:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def __provider_generated(self):
        pass

    @abstractmethod
    def __type_generated(self):
        pass

    @abstractmethod
    def __direction_generated(self):
        pass

    @abstractmethod
    def __id_generated(self):
        pass

    @abstractmethod
    def __price_generated(self):
        pass

    @abstractmethod
    def __currency_generated(self):
        pass
