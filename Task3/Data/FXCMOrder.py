from Order import Order


class FXCMOrder(Order):
    __id = ""
    __type = ""
    __price = 0
    __direction = ""
    __status = ""
    __date_time = ""
    __provider = ""
    __description = ""
    __currency = ""

    def get_id(self):
        return self.__id

    def set_id(self, _id):
        self.__id = _id

    def get_type(self):
        return self.__type

    def set_type(self, _type):
        self.__type = _type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_provider(self):
        return self.__provider

    def set_provider(self, provider):
        self.__provider = provider

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def set_order_fxcm(self, provider, _id, _type, price, direction, description, currency, date_time, status):
        self.__id = _id
        self.__type = _type
        self.__price = price
        self.__direction = direction
        self.__status = status
        self.__date_time = date_time
        self.__provider = provider
        self.__description = description
        self.__currency = currency

    def get_insert_request(self):
        return '{ ' \
               'provider:"' + self.get_provider() + \
               '", id:"' + self.get_id() + \
               '", type:"' + self.get_type() + \
               '", price:"' + self.get_price() + \
               '", direction:"' + self.get_direction() + \
               '", currency:"' + self.get_currency() + \
               '", date: new Date("' + self.get_date_time() + '")' + \
               ', status:"' + self.get_status() + \
               '"}'
