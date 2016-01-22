import string,random,Orders

class FXOpenOrder(Orders.Orders):
	
	def __init__(self):
		self.durations = ['Immediate or cancel', 'Good Till Cancel']
        
	def provider(self):
		return '~'
	def duration(self):
		return self.durations[random.randint(0,1)]
	def comment_length(self):
		return '30'
	
	def __randstring(self):
    		return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(30)])

	def comment(self):
		return "comment"
	
	def tag_length(self):
		return '10'

	def tag(self):
		return "tag"

	def magicalNumber(self):
		return str(random.randint(100000, 999999))
