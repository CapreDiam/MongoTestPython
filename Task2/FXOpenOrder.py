import string,random

class FXOpenOrder:
durations = ['Immediate or cancel', 'Good Till Cancel']
	
	def __init__(self):
		return [provider(),duration(),comment_length(),comment(),tag_length(),tag(),magicalNumber()]	
	def provider(self):
		return '*'
	def duration(self):
		return durations[random.randint(0,1)]
	def comment_length(self):
		return 30
	
	def __randstring(self):
    		return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(30)])

	def comment(self):
		return randstring()
	
	def tag_length(self):
		return 10

	def tag(self):
		return randstring()

	def magicalNumber(self):
		return str(random.randint(100000, 999999))
