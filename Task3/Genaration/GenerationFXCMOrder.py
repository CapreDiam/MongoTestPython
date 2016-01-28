import random
import uuid

from GenerationOrder import GenerationOrder


class GenerationFXCMOrder(GenerationOrder):
    directions = ['sell', 'buy']
    durations = ['Immediate or cancel', 'Good Till Cancel']
    currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY', 'CHF/JPY',
                 'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NZD', 'GBP/AUD', 'GBP/CHF', 'GBP/JPY',
                 'NZD/JPY', 'EUR/USD', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'USD/JPY', 'USD/CHF', 'USD/CAD']

    def __init__(self):
        print "FXCM"

    def __description_generated(self):
        return 'description'

    def _GenerationOrder__provider_generated(self):
        return '~'

    def _GenerationOrder__type_generated(self):
        return 'market'

    def _GenerationOrder__direction_generated(self):
        self.direction = self.directions[random.randint(0, 1)]
        return self.direction

    def _GenerationOrder__id_generated(self):
        id = str(uuid.uuid4())
        id = id[0:7] + id[24:32]
        return id

    def _GenerationOrder__price_generated(self):
        price = str(random.randint(100000, 999999) + random.random())
        return price

    def _GenerationOrder__currency_generated(self):
        return self.currencys[random.randint(0, 21)]

    def get_generated_fxcm(self):
        return {
            "id": self._GenerationOrder__id_generated(),
            "provider": self._GenerationOrder__provider_generated(),
            "type": self._GenerationOrder__type_generated(),
            "direction": self._GenerationOrder__direction_generated(),
            "price": self._GenerationOrder__price_generated(),
            "currency": self._GenerationOrder__currency_generated(),
            "description": self.__description_generated()
        }
