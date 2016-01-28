import random
import uuid


class GenerationOrder:

    def __init__(self):
        pass

    currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY', 'CHF/JPY',
                     'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NZD', 'GBP/AUD', 'GBP/CHF', 'GBP/JPY',
                     'NZD/JPY', 'EUR/USD', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'USD/JPY', 'USD/CHF', 'USD/CAD']

    def provider_generated(self):
        return '+'

    def type_generated(self):
        return 'market'

    def direction_generated(self):
        directions = ['sell', 'buy']
        direction = directions[random.randint(0, 1)]
        return direction

    def id_generated(self):
        id = str(uuid.uuid4())
        id = id[0:7] + id[24:32]
        return id

    def price_generated(self):
        price = str(random.randint(100000, 999999) + random.random())
        return price

    def currency_generated(self):
        return self.currencys[random.randint(0, 21)]
