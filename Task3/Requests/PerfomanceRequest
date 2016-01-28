import commands
class PerfomanceRequest():
    
    result_request=[]
    
    def insert_request(self, string_insert):
        operation = "echo '" + string_insert + "' > .q && mongo < .q"
        return commands.getoutput(operation)
        
    def get_result(self):
        return self.result_request
