import datetime
import random

from GenerationFXCM import GenerationFXCMOrder
from GenerationFXOpenOrder import GenerationFXOpenOrder


class GenerationStatusTime(GenerationFXCMOrder, GenerationFXOpenOrder):
    status = [["New", "To Provider", "Partially Filled", "Filled"], ["New", "To Provider", "Filled"],
              ["New", "Filled"], ["New", "Partially Filled", "To Provider", "Filled"],
              ["New", "Partially Filled", "To Provider", "Rejected", "Filled"], ["To Provider"],
              ["To Provider", "Rejected"], ["To Provider", "Filled"], ["New", "To Provider"],
              ["New", "To Provider", "Rejected"], ["New", "Partially Filled"], ["New"],
              ["New", "To Provider", "Partially Filled"]]
    fxopen_dictionary = {}
    fxcm_dictionary = {}



    def get_date_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S.%f")

    def get_status(self):
        return self.status[random.randint(0, 12)]


    def get_fxcm_dictionary(self):
        return self.get_generated_fxcm()

    def get_fxopen_dictionary(self):
        return self.get_generated_fxopen()
