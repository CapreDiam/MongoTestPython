from datetime import datetime
from Request import Request
import json


class Result(Request):
    result_python = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def compare_result(self):
        print 'Compare Result'

    def result_data(self):
        dtfirst = datetime.strptime('2016-1-15 9:12:24.25', '%Y-%m-%d %H:%M:%S.%f')
        dtsecund = datetime.strptime('2016-1-15 9:12:24.725', '%Y-%m-%d %H:%M:%S.%f')

        id = (self.count_status_by_id()).split()
        id_first = (id[10].split('"'))[1]  # result number 13
        id_second = (id[18].split('"'))[1]  # result 21
        id_third = (id[26].split('"'))[1]  # result 29
        size = int(self.redis_connector.get("size"))
        for i in range(size):
            json_string = json.loads(self.sereliazation.deserialization(self.redis_connector.get('json' + str(i))))
            # Sum count each status
            if json_string["status"] == "New":
                self.result_python[0] += 1
            elif json_string["status"] == "To Provider":
                self.result_python[1] += 1
            elif json_string["status"] == "Partially Filled":
                self.result_python[2] += 1
            elif json_string["status"] == "Filled":
                self.result_python[3] += 1
            else:
                self.result_python[4] += 1
            # sum price for each provider
            if json_string["provider"] == "*":
                self.result_python[5] += float(json_string["price"])
            else:
                self.result_python[6] += float(json_string["price"])
            # count id, status order
            if json_string["id"] == id_first:
                self.result_python[7] += 1
            elif json_string["id"] == id_second:
                self.result_python[8] += 1
            elif json_string["id"] == id_third:
                self.result_python[9] += 1
            # sum price between 2 date
            buff_date = datetime.strptime(json_string["date"], '%Y-%m-%d %H:%M:%S.%f')
            if buff_date >= dtfirst and buff_date <= dtsecund:
                self.result_python[10] += 1

        self.result_python[5] = round(self.result_python[5], 2)
        self.result_python[6] = round(self.result_python[6], 2)
        self.__compare_id_by_status()

    def __compare_id_by_status(self):
        for i in range(len(self.mongo_result)):
            if str(self.result_python[i]) == str(self.mongo_result[i]):
                print "Test [", i + 1, "] passed"
            else:
                print "Test [", i + 1, "] wrong"
