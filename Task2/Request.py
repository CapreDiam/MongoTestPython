from FXCMOrder import FXCMOrder
from FXOpenOrder import FXOpenOrder
from Serialization import Serialization
import commands
import random


class Request:
    def __init__(self):
        self.fxcm = FXCMOrder()
        self.fxopen = FXOpenOrder()
        self.sereliazation = Serialization()
        self.status = [["New", "To Provider", "Partially Filled", "Filled"], ["New", "To Provider", "Filled"],
                       ["New", "Filled"], ["New", "Partially Filled", "To Provider", "Filled"],
                       ["New", "Partially Filled", "To Provider", "Rejected", "Filled"], ["To Provider"],
                       ["To Provider", "Rejected"], ["To Provider", "Filled"], ["New", "To Provider"],
                       ["New", "To Provider", "Rejected"], ["New", "Partially Filled"], ["New"],
                       ["New", "To Provider", "Partially Filled"]]

    def generation_request_insert(self):
        for i in range(3000):
            if i < 1499:
                string_insert = 'db.orders.insert( { provider: ' + '"' + self.fxopen.provider() + '"' + ', id: ' + '"' + self.fxopen.id() + '"' + ', type: ' + '"' + self.fxopen.type() + '"' + ', price: ' + self.fxopen.price() + ', direction: ' + '"' + self.fxopen.direction() + '"' ', currency: ' + '"' + self.fxopen.currency() + '"' + ' ,duration: ' + '"' + self.fxopen.duration() + '"' + ' ,comment_length: ' + '"' + self.fxopen.comment_length() + '"' + ' ,comment: ' + '"' + self.fxopen.comment() + '"' + ', tag_length: ' + '"' + self.fxopen.tag_length() + '"' + ', tag: ' + '"' + self.fxopen.tag() + '"' + ' ,magic_number: ' + '"' + self.fxopen.magicalNumber() + '" ,'
            else:
                string_insert = 'db.orders.insert( { provider: ' + '"' + self.fxcm.provider() + '"' + ', id: ' + '"' + self.fxcm.id() + '"' + ', type: ' + '"' + self.fxcm.type() + '"' + ', price: ' + self.fxcm.price() + ', direction: ' + '"' + self.fxcm.direction() + '", currency: ' + '"' + self.fxcm.currency() + '"' + ', decsription: ' + '"' + self.fxcm.description() + '" ,'
            a = random.randint(0, 12)
            b = len(self.status[a])
            for j in range(b):
                string_insert_finally = string_insert + ' date: new Date(' + self.fxcm.date_time() + '), status: "' + self.status[a][j] + '" })'
                print self.__insert_request(string_insert_finally)
                string_insert_finally = ''

    def __insert_request(self, string_insert):
        operation = "echo '" + string_insert + "' > .q && mongo < .q"
        print operation
        return commands.getoutput(operation)

    def insert_request(self, string_insert):
        operation = "echo '" + string_insert + "' > .q && mongo < .q"
        commands.getoutput(operation)

    def id_by_status(self):
        statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
        for i in range(len(statuses)):
            count_statuses = "db.orders.find( { status: " + '"' + statuses[i] + '"' + " } ).count()"
            self.__insert_request(count_statuses)

    def sum_by_fxcm(self):
        sum_by_fxcm = "db.orders.aggregate( [ { $match : { provider: " + '"' + '*' + '"' + " } }, { " \
                                                                                           "$group: { _id: " + '"' + "$provider" + '"' + ", sum: { $sum: " + '"' + "$price" + '"' + " } } } ] )"
        self.__insert_request(sum_by_fxcm)

    def sum_by_fxopen(self):
        sum_by_fxopen = "db.orders.aggregate( [ { $match : { provider: " + '"' + '~' + '"' + " } }, { $group: { _id: " + '"' + "$provider" + '"' + ", " \
                                                                                                                                                   "sum: { $sum: " + '"' + "$price" + '"' + " } } } ] )"
        self.__insert_request(sum_by_fxopen)

    def status_by_id(self):
        status_by_id = "db.orders.aggregate( { $group: { _id: " + '"' + "$id" + '"' + ", count: { $sum: 1 } } }, { $limit: 3 } )"
        self.__insert_request(status_by_id)

    def between_dates(self):
        between_dates = "db.orders.aggregate( [ { $match : { date: { $gte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.25" \
                        + '"' + "),$lte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.725" + '"' + ") } } }, { $group: { _id:" \
                                                                                                                  " null, count: { $sum: 1 } } } ] )"
        self.__insert_request(between_dates)
