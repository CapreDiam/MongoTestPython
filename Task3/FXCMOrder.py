from Order import Order
class FXCMOrder(Order):
    
    _id=""
    _type=""
    _price=0
    _direction=""
    _status=""
    _date_time=""
    _provider=""
    _description="" 
        
    
    def get_id(self):
        return self._id
        
   
    def set_id(self,id):
        self._id=id
        
    
    def get_type(self):
        return self._type
        
   
    def set_type(self,type):
        self._type=type
    
    
    def get_price(self):
        return self._price
        
    
    def set_price(self,price):
        self._price=price
        
    
    def get_direction(self):
        return self._direction
        
    
    def set_direction(self,direction):
        self._direction=direction
    
    
    def get_currency(self):
        return self._currency
        
    
    def set_currency(self,currency):
        self._currency=currency
        
   
    def get_date_time(self):
        return self._date_time
        
    
    def set_date_time(self,date_time):
        self._date_time=date_time
        
    
    def get_status(self):
        return self._status
        
    
    def set_status(self,status):
        self._status=status
    
    
    def get_provider(self):
        return self._provider
        
    
    def set_provider(self,provider):
        self._provider=provider
        
  
    def get_description(self):
        return self._description
        
    
    def set_description(self,description):
        self._description=description
