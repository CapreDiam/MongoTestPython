from Order import Order
class FXOpenOrder(Order):
    
    _id=""
    _type=""
    _price=0
    _direction=""
    _status=""
    _date_time=""
    _provider=""
    _duration=""
    _comment=""
    _comment_len=""
    _tag=""
    _tag_len=""
    _magical_number=0 
        
    
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
        
        
    def get_duration(self):
        return self._duration
        
   
    def set_duration(self,duration):
        self._duration=duration
        
        
    def get_comment(self):
        return self._comment
        
   
    def set_comment(self,comment):
        self._comment=comment
    
    def get_comment_len(self):
         return self._comment_len
        
   
    def set_comment_len(self,comment_len):
        self._comment_len=comment_len
                
           
    def get_tag(self):
        return self._tag
        
   
    def set_tag(self,tag):
        self._tag=tag
    
    
    def get_tag_len(self):
        return self._tag_len
        
   
    def set_tag_len(self,tag_len):
        self._tag_len=tag_len
                    
        
    def get_magical_number(self):
        return self._magical_number
        
   
    def set_magical_number(self,magical_number):
        self._magical_number=magical_number
