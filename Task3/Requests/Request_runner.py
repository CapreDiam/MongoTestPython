from SumProvider import SumProvider
from SumBetweenDate import SumBetweenDate
from CountStatuses import CountStatuses
from CountIdStatuses import CountIdStatuses
from PerfomanceRequest import PerfomanceRequest

s=SumBetweenDate().perfomance_request()
s=SumProvider().perfomance_request()
s=CountStatuses().perfomance_request()
s=CountIdStatuses().perfomance_request()

s=PerfomanceRequest()
for i in range(len(s.result_request)):
    print (s.result_request[i])
