def date_time():
	i=0
	year='2016'
	month='01'
	day='15'
	hour='16'
	minute=24
	sec=0
	milisec=0
	file = open ('datetime', 'w')			
	while i < 3000:
		file.write(str(year)+'-'+str(month)+'-'+str(day)+'T'+str(hour)+':'+str(minute)+':'+str(sec)+'.'+str(milisec) + '\n')		
		milisec=milisec+4	
		if milisec>=1000:
			milisec=milisec-1000
			sec=sec+1
		i = i + 1
	file.close()
