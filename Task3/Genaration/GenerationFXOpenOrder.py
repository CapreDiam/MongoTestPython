import random
import string
import uuid

from GenerationOrder import GenerationOrder


class GenerationFXOpenOrder(GenerationOrder):
    directions = ['sell', 'buy']
    durations = ['Immediate or cancel', 'Good Till Cancel']
    currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY', 'CHF/JPY',
                 'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NZD', 'GBP/AUD', 'GBP/CHF', 'GBP/JPY',
                 'NZD/JPY', 'EUR/USD', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'USD/JPY', 'USD/CHF', 'USD/CAD']

    def __init__(self):
        print "FXOpen"

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
        print id, " - id"
        return id

    def _GenerationOrder__price_generated(self):
        price = str(random.randint(100000, 999999) + random.random())
        return price

    def _GenerationOrder__currency_generated(self):
        return self.currencys[random.randint(0, 21)]

    def __duration_generated(self):
        return self.durations[random.randint(0, 1)]

    def __comment_length_generated(self):
        return 10

    def __randstring(self):
        return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

    def __comment_generated(self):
        return self.__randstring()

    def __tag_length_generated(self):
        return 10

    def __tag_generated(self):
        return self.__randstring()

    def __magical_number_generated(self):
        return 1000000

    def get_generated_fxopen(self):
        return {
            "id": self._GenerationOrder__id_generated(),
            "provider": self._GenerationOrder__provider_generated(),
            "type": self._GenerationOrder__type_generated(),
            "direction": self._GenerationOrder__direction_generated(),
            "price": self._GenerationOrder__price_generated(),
            "currency": self._GenerationOrder__currency_generated(),
            "duration": self.__duration_generated(),
            "comment_length": self.__comment_length_generated(),
            "comment": self.__comment_generated(),
            "tag_length": self.__tag_length_generated(),
            "tag": self.__tag_generated(),
            "magical_number": self.__magical_number_generated()
        }
