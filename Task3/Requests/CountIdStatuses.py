from PerfomanceRequest import PerfomanceRequest
import re

class CountIdStatuses(PerfomanceRequest):
    
    string_insert = "db.orders.aggregate( { $group: { _id: "+'"'+"$id"+'"'+", count: { $sum: 1 } } }, { $limit: 3 } )"
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        
        res=self.insert_request(self.string_insert)
        self.prepare_result(res)                                                                                
        
    
    def prepare_result(self,res):
        result=re.findall(r'[1-9]+\n',res)
        
        for i in range(len(result)-2):
            results=result[i+1]
            
            self.result_request.append(results)
