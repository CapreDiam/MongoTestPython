from Order import Order


class FXOpenOrder(Order):
    __id = ""
    __type = ""
    __price = 0
    __direction = ""
    __status = ""
    __date_time = ""
    __provider = ""
    __duration = ""
    __comment = ""
    __comment_len = 0
    __tag = ""
    __tag_len = 0
    __magical_number = 0
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

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        self.__comment = comment

    def get_comment_length(self):
        return self.__comment_len

    def set_comment_length(self, comment_len):
        self.__comment_len = comment_len

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    def get_tag_length(self):
        return self.__tag_len

    def set_tag_length(self, tag_len):
        self.__tag_len = tag_len

    def get_magical_number(self):
        return self.__magical_number

    def set_magical_number(self, magical_number):
        self.__magical_number = magical_number

    def set_order_fxopen(self, _id, _type, price, direction, provider, duration,
                         comment, comment_len, tag, tag_len, magical_number, currency, status, date_time):
        self.__id = _id
        self.__type = _type
        self.__price = price
        self.__direction = direction
        self.__status = status
        self.__date_time = date_time
        self.__provider = provider
        self.__duration = duration
        self.__comment = comment
        self.__comment_len = comment_len
        self.__tag = tag
        self.__tag_len = tag_len
        self.__magical_number = magical_number
        self.__currency = currency

    def get_insert_request(self):
        return '{ ' \
               'provider:"' + self.get_provider() + \
               '", id:"' + self.get_id() + \
               '", type:"' + self.get_type() + \
               '", price:"' + str(self.get_price()) + \
               '", direction:"' + self.get_direction() + \
               '", currency:"' + self.get_currency() + \
               '", duration:"' + self.get_duration() + \
               '", comment_length:"' + str(self.get_comment_length()) + \
               '", comment:"' + self.get_comment() + \
               '", tag_length:"' + str(self.get_tag_length()) + \
               '", tag:"' + self.get_tag() + \
               '", date: new Date("' + self.get_date_time() + '")' + \
               ', status:"' + self.get_status() + '"}'
