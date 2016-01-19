def checkHMS(HMSchek, HMSincr):
	if((HMSchek[0]+1) == 60):
		HMSchek[0] = 0
		HMSincr[0] = HMSincr[0] + 1

def date_time():
	i=0
	year=2016
	month=1
	day=15
	timeArray=[9,12,24]
	hours=[9]
	minute=[12]
	second=[24]
	millisecond=[1]
	file = open('datetime.txt', 'w')
	while i < 9999:
		file.write('"' + str(year) + '\\' + str(month) + '\\' + str(day) +\
		' '+ str(hours[0]) + ':' + str(minute[0]) + ':' + str(second[0]) +\
		'.' + str(millisecond[0])+'"' +'\n')
		i = i + 1
		if((millisecond[0]+10)>999):
			millisecond[0]=1
			second[0] = second[0] + 1
		'''if((second)==60):
			second=0
			minute = minute + 1
		if((minute)==60):
			minute=0
			hours = hours + 1'''
		millisecond[0] = millisecond[0] + 4
		checkHMS(second,minute)
		checkHMS(second,minute)
	file.close()	

