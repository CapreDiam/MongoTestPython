import random
def status_gen():
	order='наш склеен запрос'
	status = [['New','To Provider','Partially Filled','Filled'],['New', 'To Provider', 'Filled']]#для примера 2 выбора статуса
	i=0
	file=open('result','w')
	while i<5:
		a=random.randint(0,1)#выбор м-у двумя статусами
		b=len(status[a])
		for x in b:		
			OurOrder = order + status[a][x]
			file.write(OurOrder+'/n')
	file.close()	
