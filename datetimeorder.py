def date_time():
	i=0
	year=2016
	month=1
	day=15
	hours=9
	minute=12
	second=24
	millisecond=1
	file = open('datetime.txt', 'w')
	while i < 9999:
		file.write('"' + str(year) + '\\' + str(month) + '\\' + str(day) +' '+ str(hours) + ':' + str(minute) + ':' + str(second) + '.' + str(millisecond)+'"' +'\n')
		i = i + 1
		if((millisecond+10)>999):
			millisecond=1
			second = second + 1
		if((second)==60):
			second=0
			minute = minute + 1
		if((minute)==60):
			minute=0
			hours = hours + 1
		millisecond = millisecond + 4
	file.close()	

def chekHMS(HMSchek, HMSincr):
	if((HMSchek+1) == 60):
		HMSchek = 0
		HMSincr = HMSincr + 1
