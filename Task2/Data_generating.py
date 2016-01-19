import random
import uuid
import string

class generation:
	
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
