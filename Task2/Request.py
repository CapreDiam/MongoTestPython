from FXCMOrder import FXCMOrder
from FXOpenOrder import FXOpenOrder
from Serialization import Serialization
import commands
import random
import redis


class Request:
    def __init__(self):
        self.fxcm = FXCMOrder()
        self.fxopen = FXOpenOrder()
        self.sereliazation = Serialization()
        self.redis_connector = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.status = [["New", "To Provider", "Partially Filled", "Filled"], ["New", "To Provider", "Filled"],
                       ["New", "Filled"], ["New", "Partially Filled", "To Provider", "Filled"],
                       ["New", "Partially Filled", "To Provider", "Rejected", "Filled"], ["To Provider"],
                       ["To Provider", "Rejected"], ["To Provider", "Filled"], ["New", "To Provider"],
                       ["New", "To Provider", "Rejected"], ["New", "Partially Filled"], ["New"],
                       ["New", "To Provider", "Partially Filled"]]
        self.mongo_result = []

    def __prepare_data_mongo(self):
        self.id_by_status()
        self.sum_by_fxcm()
        self.sum_by_fxopen()
        self.count_status_by_id_result()
        self.between_dates()

    def __insert_request(self, string_insert):
        operation = "echo '" + string_insert + "' > .q && mongo < .q"
        return commands.getoutput(operation)

    def generation_request_insert(self):
        x = 0
        for i in range(100):
            if i < 50:
                string_insert = 'db.orders.insert( { "provider": ' + '"' + self.fxopen.provider() + '"' + ', "id": ' + '"' + self.fxopen.id() + '"' + ', "type": ' + '"' + self.fxopen.type() + '"' + ', "price": ' + self.fxopen.price() + ', "direction": ' + '"' + self.fxopen.direction() + '"' ', "currency": ' + '"' + self.fxopen.currency() + '"' + ' ,"duration": ' + '"' + self.fxopen.duration() + '"' + ' ,"comment_length": ' + '"' + self.fxopen.comment_length() + '"' + ' ,"comment": ' + '"' + self.fxopen.comment() + '"' + ', "tag_length": ' + '"' + self.fxopen.tag_length() + '"' + ', "tag": ' + '"' + self.fxopen.tag() + '"' + ' ,"magic_number": ' + '"' + self.fxopen.magicalNumber() + '" ,'
            else:
                string_insert = 'db.orders.insert( { "provider": ' + '"' + self.fxcm.provider() + '"' + ', "id": ' + '"' + self.fxcm.id() + '"' + ', "type": ' + '"' + self.fxcm.type() + '"' + ', "price": ' + self.fxcm.price() + ', "direction": ' + '"' + self.fxcm.direction() + '", "currency": ' + '"' + self.fxcm.currency() + '"' + ', "description": ' + '"' + self.fxcm.description() + '" ,'
            a = random.randint(0, 12)
            b = len(self.status[a])
            for j in range(b):
                date = self.fxcm.date_time()
                string_insert_finally = string_insert + ' "date": new Date(' + date + '), "status": "' + self.status[a][
                    j] + '" })'
                json_insert = string_insert[17:len(string_insert)] + ' "date":' + date + ', "status": "' + \
                              self.status[a][j] + '" }'
                self.redis_connector.set("json" + str(x), self.sereliazation.serialization(json_insert))
                self.__insert_request(string_insert_finally)
                string_insert_finally = ''
                x += 1
        self.redis_connector.set("size", x)
        self.__prepare_data_mongo()

    def insert_request(self, string_insert):
        operation = "echo '" + string_insert + "' > .q && mongo < .q"
        commands.getoutput(operation)

    def id_by_status(self):
        result = []
        statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
        for i in range(len(statuses)):
            count_statuses = "db.orders.find( { status: " + '"' + statuses[i] + '"' + " } ).count()"
            result.append(((self.__insert_request(count_statuses)).split())[7])
        self.__append_result(result)

    def sum_by_fxcm(self):
        sum_by_fxcm = "db.orders.aggregate( [ { $match : { provider: " + '"' + '*' + '"' + " } }, { " \
                                                                                           "$group: { _id: " + '"' + "$provider" + '"' + ", sum: { $sum: " + '"' + "$price" + '"' + " } } } ] )"
        self.__append_result([round(float(((self.__insert_request(sum_by_fxcm)).split())[13]), 2)])

    def sum_by_fxopen(self):
        sum_by_fxopen = "db.orders.aggregate( [ { $match : { provider: " + '"' + '~' + '"' + " } }, { $group: { _id: " + '"' + "$provider" + '"' + ", " \
                                                                                                                                                   "sum: { $sum: " + '"' + "$price" + '"' + " } } } ] )"
        self.__append_result([round(float(((self.__insert_request(sum_by_fxopen)).split())[13]), 2)])

    def count_status_by_id(self):
        status_by_id = "db.orders.aggregate( { $group: { _id: " + '"' + "$id" + '"' + ", count: { $sum: 1 } } }, { $limit: 3 } )"
        return self.__insert_request(status_by_id)

    def count_status_by_id_result(self):
        result = []
        status_by_id = "db.orders.aggregate( { $group: { _id: " + '"' + "$id" + '"' + ", count: { $sum: 1 } } }, { $limit: 3 } )"
        count_id = self.__insert_request(status_by_id)
        result.append((count_id.split())[13])
        result.append((count_id.split())[21])
        result.append((count_id.split())[29])
        self.__append_result(result)

    def between_dates(self):
        between_dates = "db.orders.aggregate( [ { $match : { date: { $gte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.25" \
                        + '"' + "),$lte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.725" + '"' + ") } } }, { $group: { _id:" \
                                                                                                                " null, count: { $sum: 1 } } } ] )"
        self.__append_result([((self.__insert_request(between_dates)).split())[13]])


    def __append_result(self, result):
        self.mongo_result.extend(result)
