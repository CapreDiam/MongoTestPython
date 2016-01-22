import Orders
class FXCMOrder(Orders.Orders):
		
	def provider(self):
		return '*'
	
	def decsription(self):
		return 'description'
