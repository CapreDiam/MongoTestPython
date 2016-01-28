from PerfomanceRequest import PerfomanceRequest

class CountIdStatuses(PerfomanceRequest):
    
    
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        string_insert = "db.orders.aggregate( { $group: { _id: " + '"' + "$id" + '"' + ", count: { $sum: 1 } } }, { $limit: 3 } )"
        self.result_request.append(((self.insert_request(string_insert)).split())[7])
    
    def prepare_result(self):
        pass
