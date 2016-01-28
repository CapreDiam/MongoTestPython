from PerfomanceRequest import PerfomanceRequest

class SumProvider(PerfomanceRequest):
    
    
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        providers = ['~','*']
        for i in range(len(statuses)):
             string_insert = "db.orders.aggregate( [ { $match : { provider: " + '"' + providers[i] + '"' + " } }, { " "$group: { _id: " + '"' + "$provider" + '"' + ", sum: { $sum: " + '"' + "$price" + '"' + " } } } ] )"
             self.result_request([round(((self.insert_request(string_insert)).split())[13], 2)])
        
    def prepare_result(self):
        pass
