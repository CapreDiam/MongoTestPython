from OrdersData.FXCMOrder import FXCMOrder
from OrdersData.FXOpenOrders import FXOpenOrder
from Generation.Orders.GenerationStatusTime import GenerationStatusTime
from Generation.Insert.GenerationInsert import GenerationInsert

class GenerationDataOrder:



    def __init__(self):
        self.__fxopen_dict = {}
        self.__fxcm_dict = {}
        self.__status = []
        self.__fxcm = FXCMOrder()
        self.__fxopen = FXOpenOrder()
        self.__status_time = GenerationStatusTime()
        self.__size = 1000
        self.__list_orders_fxopen = []
        self.__list_orders_fxcm = []
        self.__list_orders = []
        self.insert = GenerationInsert()


    def __set_fxopen_order(self):
        count = 0
        for i in range(self.__size):
            self.__fxopen_dict = self.__status_time.get_generated_fxopen()
            self.__status = self.__status_time.get_status()
            for j in range(len(self.__status)):
                self.__list_orders_fxopen.append(FXOpenOrder())
                self.__list_orders_fxopen[count].set_order_fxopen(self.__fxopen_dict.get("id"),
                                                                  self.__fxopen_dict.get("type"),
                                                                  self.__fxopen_dict.get("price"),
                                                                  self.__fxopen_dict.get("direction"),
                                                                  self.__fxopen_dict.get("provider"),
                                                                  self.__fxopen_dict.get("duration"),
                                                                  self.__fxopen_dict.get("comment"),
                                                                  self.__fxopen_dict.get("comment_length"),
                                                                  self.__fxopen_dict.get("tag"),
                                                                  self.__fxopen_dict.get("tag_length"),
                                                                  self.__fxopen_dict.get("magical_number"),
                                                                  self.__fxopen_dict.get("currency"),
                                                                  self.__status[j],
                                                                  self.__status_time.get_date_time())
                count += 1
        self.__append(self.__list_orders_fxopen)
        count = 0
        for i in range(self.__size):
            self.__fxcm_dict = self.__status_time.get_generated_fxcm()
            self.__status = self.__status_time.get_status()
            for j in range(len(self.__status)):
                self.__list_orders_fxcm.append(FXCMOrder())
                self.__list_orders_fxcm[count].set_order_fxcm(self.__fxcm_dict.get("provider"),
                                                              self.__fxcm_dict.get("id"),
                                                              self.__fxcm_dict.get("type"),
                                                              self.__fxcm_dict.get("price"),
                                                              self.__fxcm_dict.get("direction"),
                                                              self.__fxcm_dict.get("description"),
                                                              self.__fxcm_dict.get("currency"),
                                                              self.__status_time.get_date_time(),
                                                              self.__status[j])
                count += 1
        self.__append(self.__list_orders_fxcm)

    def __set_fxcm_order(self):
        count = 0
        for i in range(self.__size):
            self.__fxcm_dict = self.__status_time.get_generated_fxcm()
            self.__status = self.__status_time.get_status()
            for j in range(len(self.__status)):
                self.__list_orders_fxcm.append(FXCMOrder())
                self.__list_orders_fxcm[count].set_order_fxcm(self.__fxcm_dict.get("provider"),
                                                              self.__fxcm_dict.get("id"),
                                                              self.__fxcm_dict.get("type"),
                                                              self.__fxcm_dict.get("price"),
                                                              self.__fxcm_dict.get("direction"),
                                                              self.__fxcm_dict.get("description"),
                                                              self.__fxcm_dict.get("currency"),
                                                              self.__status_time.get_date_time(),
                                                              self.__status[j])
                count += 1
        self.__append(self.__list_orders_fxcm)

    def generation_data(self):
        print 'generation data'
        self.insert.prepare_db()
        self.__set_fxopen_order()
        self.insert.set_orders(self.__list_orders)

    def __append(self, _list):
        self.__list_orders.extend(_list)

a = GenerationDataOrder()
a.generation_data()
