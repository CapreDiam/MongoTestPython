from PerfomanceRequest import PerfomanceRequest

class CountStatuses(PerfomanceRequest):
    
    
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
        for i in range(len(statuses)):
            string_insert = "db.orders.find( { status: " + '"' + statuses[i] + '"' + " } ).count()"
            self.result_request.append(((self.insert_request(string_insert)).split())[7])
    
    def prepare_result(self):
        pass
