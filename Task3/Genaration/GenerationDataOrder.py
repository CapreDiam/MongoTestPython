from FXCMOrder import FXCMOrder 
from FXOpenOrder import FXOpenOrder

class GenerationDataOrder():
    __fxcm=FXCMOrder()
    __fxopen=FXOpenOrder()
    __list_orders=[]
    
    def get_list_orders(self):
        return __list_orders
    
    def __set_fxcm_order(self):
        self.__list_orders.append(self.__fxcm)
        
    def __set_fxopen_order(self):
        self.__list_orders.append(self.__fxopen)
