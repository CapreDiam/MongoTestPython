from abc import ABCMeta, abstractmethod
class Order:
    __metaclass__=ABCMeta
        
    @abstractmethod
    def get_id(self):
        pass
        
    @abstractmethod
    def set_id(self,id):
        pass
        
    @abstractmethod
    def get_type(self):
        pass
        
    @abstractmethod
    def set_type(self,type):
        pass
    
    @abstractmethod
    def get_price(self):
        pass
        
    @abstractmethod
    def set_price(self,price):
        pass
    @abstractmethod
    def get_direction(self):
        pass
        
    @abstractmethod
    def set_direction(self,direction):
        pass
    
    @abstractmethod
    def get_currency(self):
        pass
        
    @abstractmethod
    def set_currency(self,currency):
        pass
        
    @abstractmethod
    def get_date_time(self):
        pass
        
    @abstractmethod
    def set_date_time(self,date_time):
        pass
        
    @abstractmethod
    def get_status(self):
        pass
        
    @abstractmethod
    def set_status(self,status):
        pass
    
    @abstractmethod
    def get_provider(self):
        pass
        
    @abstractmethod
    def set_provider(self,provider):
        pass
