from TestsMongo import TestsMongo
from TestsPython import TestsPython

class CompareTests(TestsMongo,TestsPython)
    _resultMongo=TestsMongo().results
    _resultPython=TestsPython().results
    _result=[]
    
    def start_compare(self):
        for i in range(len(self._resultMongo)):
            if str(self._resultPython[i]) == str(self._resultMongo[i]):
                res="Test [", i + 1, "] passed"
            else:
                res="Test [", i + 1, "] wrong"
            self._result.append(res)
            
    def get_result(self):
        return self._result
                
    def print_result(self):
        for i in range(len(self._result)):
            print self._result[i]
