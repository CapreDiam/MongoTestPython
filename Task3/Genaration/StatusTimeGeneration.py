class StatusTimeGeneration():
    class Orders:
        year = 2016
        month = 1
        day = 15
        hours = [9]
        minute = [12]
        second = [24]
        millisecond = [1]
        status = [["New", "To Provider", "Partially Filled", "Filled"], ["New", "To Provider", "Filled"],
                       ["New", "Filled"], ["New", "Partially Filled", "To Provider", "Filled"],
                       ["New", "Partially Filled", "To Provider", "Rejected", "Filled"], ["To Provider"],
                       ["To Provider", "Rejected"], ["To Provider", "Filled"], ["New", "To Provider"],
                       ["New", "To Provider", "Rejected"], ["New", "Partially Filled"], ["New"],
                       ["New", "To Provider", "Partially Filled"]]
                        
    def __checkHMS(self, HMSchek, HMSincr):
        if ((HMSchek[0] + 1) == 60):
            HMSchek[0] = 0
            HMSincr[0] = HMSincr[0] + 1

    def date_time_generation(self):
        datetime = '"' + str(self.year) + '-' + str(self.month) + '-' + str(self.day) + \
                   ' ' + str(self.hours[0]) + ':' + str(self.minute[0]) + ':' + str(self.second[0]) + \
                   '.' + str(self.millisecond[0]) + '"'
        if ((self.millisecond[0] + 5) > 999):
            self.millisecond[0] = 1
        self.millisecond[0] = self.millisecond[0] + 4
        self.__checkHMS(self.second, self.minute)
        self.__checkHMS(self.minute, self.hours)
        return datetime
    
    def status_generation(self):
        a = random.randint(0, 12)
        b = len(self.status[a])
        for j in range(b):
            date = self.date_time_generation()
            string_insert_finally = string_insert + ' "date": new Date(' + date + '), "status": "' + self.status[a][
                    j] + '" })'
    
    def get_time_status(self):
