import random
import uuid


class Orders:
    def __init__(self):
        self.year = 2016
        self.month = 1
        self.day = 15
        self.hours = [9]
        self.minute = [12]
        self.second = [24]
        self.millisecond = [1]

    def provider(self):
        return '+'

    def type(self):
        return 'market'

    def direction(self):
        directions = ['sell', 'buy']
        direction = directions[random.randint(0, 1)]
        return direction

    def id(self):
        id = str(uuid.uuid4())
        id = id[0:7] + id[24:32]
        return id

    def price(self):
        price = str(random.randint(100000, 999999) + random.random())
        return price

    def currency(self):
        currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY', 'CHF/JPY',
                     'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'EUR/NZD', 'GBP/AUD', 'GBP/CHF', 'GBP/JPY',
                     'NZD/JPY', 'EUR/USD', 'GBP/USD', 'AUD/USD', 'NZD/USD', 'USD/JPY', 'USD/CHF', 'USD/CAD']
        return currencys[random.randint(0, 21)]

    def __checkHMS(self, HMSchek, HMSincr):
        if ((HMSchek[0] + 1) == 60):
            HMSchek[0] = 0
            HMSincr[0] = HMSincr[0] + 1

    def date_time(self):
        datetime = '"' + str(self.year) + '-' + str(self.month) + '-' + str(self.day) + \
                   ' ' + str(self.hours[0]) + ':' + str(self.minute[0]) + ':' + str(self.second[0]) + \
                   '.' + str(self.millisecond[0]) + '"'
        if ((self.millisecond[0] + 5) > 999):
            self.millisecond[0] = 1
        self.millisecond[0] = self.millisecond[0] + 4
        self.__checkHMS(self.second, self.minute)
        self.__checkHMS(self.minute, self.hours)
        return datetime
