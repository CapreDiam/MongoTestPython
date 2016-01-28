from abc import ABCMeta, abstractmethod


class GenerationOrder:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def provider_generated(self):
        pass

    @abstractmethod
    def type_generated(self):
        pass

    @abstractmethod
    def direction_generated(self):
        pass

    @abstractmethod
    def id_generated(self):
        pass

    @abstractmethod
    def price_generated(self):
        pass

    @abstractmethod
    def currency_generated(self):
        pass
