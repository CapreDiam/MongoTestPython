import random
import uuid
import string

class generation:

	def datetime(self):
		i=0
		year=2016
		month=1
		day=15
		timeArray=[9,12,24]
		hours=[9]
		minute=[12]
		second=[24]
		millisecond=[1]
		file = open('datatime','w')
		while i < 9999:
			file.write(str(year) + '\\' + str(month) + '\\' + str(day) +\
			' '+ str(hours[0]) + ':' + str(minute[0]) + ':' + str(second[0]) +\
			'.' + str(millisecond[0])+'"' +'\n')
			i = i + 1
			if((millisecond[0]+10)>999):
				millisecond[0]=1
				second[0] = second[0] + 1
			if((second[0]+1)==60):
				second[0] = 0
				minute[0] = minute[0]+1
			millisecond[0] = millisecond[0] + 4
		file.close()
			
					
				
	

	def id(self):
		id=str(uuid.uuid4())
		idq=id[0:7] + id[24:32]
		return idq
	
	def type(self):
		return "market"

	def size(self):
		sizes = str(random.randint(100000, 999999)+random.random())
		return sizes
		 	
	def tag(self):
		a = string.ascii_letters + string.digits
   		return ''.join([random.choice(a) for i in range(10)])

	def lentag(self):
		return "10"

	def magicnum(self):
		number = str(random.randint(100000, 999999))
		return number
	
	def currency(self):
		currencys = ['AUD/CHF', 'AUD/JPY', 'AUD/NZD', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'AUD/JPY', 'CAD/JPY','CHF/JPY','EUR/AUD','EUR/CAD','EUR/CHF','EUR/GBP','EUR/JPY','EUR/NZD','GBP/AUD','GBP/CHF','GBP/JPY','NZD/JPY','EUR/USD','GBP/USD','AUD/USD','NZD/USD','USD/JPY','USD/CHF','USD/CAD']
		currencyq = currencys[random.randint(0,21)]
		return currencyq
	
	def comment(self):
		a = string.ascii_letters + string.digits
    		return ''.join([random.choice(a) for i in range(30)])
	
	def lencom(self):	
		return "30"

	def duration(self):
		durations = ['Immediate or cancel', 'Good Till Cancel']
		duration = durations[random.randint(0,1)]
		return duration

	def direction(self):
		directions = ['sell', 'buy']
		directionq = directions[random.randint(0,1)]
		return directionq
	
	def description(self):
		a = string.ascii_letters + string.digits
		return ''.join([random.choice(a) for i in range(40)])


	def status(self,query):
		dt = generation().datetime()
		file = open('examlpe','a')
		file2 = open('datatime','r')
		dd=file2.readlines()
        	file2.close()
		status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
		a=random.randint(0,12)
		b=len(status[a])
		
		for x in range(b):
			done=str(query[0:len(query)-1]) + "date: new Date("+'"'+str(dt[0:len(dt)-1])+'), '+"status: "+ '"'+status[a][x]+'"'+' }'+' )'+'\n'
			file.write(done+'\n')
			
			
     		

	
	
	
		
