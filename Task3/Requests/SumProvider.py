from PerfomanceRequest import PerfomanceRequest
import re
class SumProvider(PerfomanceRequest):
    
    providers = ['~','*']
    
    def get_result_request(self):
        return self.result_request
        
    def perfomance_request(self):
        
        for i in range(len(self.providers)):
             string_insert = "db.orders.aggregate( [ { $match : { provider: "+'"'+self.providers[i]+'"'+" } }, { $group: { _id: "+'"'+"$provider"+'"'+", sum: { $sum: "+'"'+"$price"+'"'+" } } } ] )"
             res=self.insert_request(string_insert)
             self.prepare_result(res)
             
        
    def prepare_result(self,res):
        result=re.findall(r'\{.+\}',res)
        result=result[0]
        
        self.result_request.append(result)
