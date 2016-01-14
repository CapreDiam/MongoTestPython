def gener_type():
	i=0	
	file = open('types.txt', 'w')
	while i < 3000:
		file.write('market'+ '\n')
		i = i + 1
	file.close()	
