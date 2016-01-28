from PerfomanceRequest import PerfomanceRequest

class SumBetweenDate(PerfomanceRequest):
    
    a=PerfomanceRequest()
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        string_result="db.orders.aggregate( [ { $match : { date: { $gte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.25" \
                        + '"' + "),$lte: new Date(" + '"' + "2016" + '-' + "1" + '-' + "15 9:12:24.725" + '"' + ") } } }, { $group: { _id:" \
                                                                                                                " null, count: { $sum: 1 } } } ] )"
        self.result_request.append([(self.insert_request(string_result)).split()[13]])
    
    def prepare_result(self):
        pass
