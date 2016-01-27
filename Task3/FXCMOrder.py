from abc import ABCMeta, abstractmethod
from Order import Order
class FXCMOrder(Order):
    __metaclass__=ABCMeta
    id=""
    type=""
    price=0
    direction=""
    status=""
    date_time=""
    provider=""
        
    @abstractmethod
    def get_id(self):
        return self._id
        
    @abstractmethod
    def set_id(self,id):
        self._id=id
        
    @abstractmethod
    def get_type(self):
        return self._type
        
    @abstractmethod
    def set_type(self,type):
        self._type=type
    
    @abstractmethod
    def get_price(self):
        return self._price
        
    @abstractmethod
    def set_price(self,price):
        self._price=price
        
    @abstractmethod
    def get_direction(self):
        return self._direction
        
    @abstractmethod
    def set_direction(self,direction):
        self._direction=direction
    
    @abstractmethod
    def get_currency(self):
        return self._currency
        
    @abstractmethod
    def set_currency(self,currency):
        self._currency=currency
        
    @abstractmethod
    def get_date_time(self):
        return self._date_time
        
    @abstractmethod
    def set_date_time(self,date_time):
        self._date_time=date_time
        
    @abstractmethod
    def get_status(self):
        return self._status
        
    @abstractmethod
    def set_status(self,status):
        self._status=status
    
    @abstractmethod
    def get_provider(self):
        return self._provider
        
    @abstractmethod
    def set_provider(self,provider):
        self._provider=provider
