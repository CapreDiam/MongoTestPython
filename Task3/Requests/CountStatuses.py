from PerfomanceRequest import PerfomanceRequest
import re

class CountStatuses(PerfomanceRequest):
    
    statuses = ["New", "To Provider", "Partially Filled", "Filled", "Rejected"]
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        
        for i in range(len(self.statuses)):
            string_insert = "db.orders.find( { status: " + '"' + self.statuses[i] + '"' + " } ).count()"
            res=self.insert_request(string_insert)
            self.prepare_result(res)
            
    
    def prepare_result(self,res):
        result=re.findall(r'\n[1-9]+',res)
        result=result[0]
                                                                                           
        self.result_request.append(result)
