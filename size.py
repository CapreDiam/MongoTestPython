import random

def generate_size():
	i=0
	file = open('size.txt', 'w')
	while i < 3000:
		size=str(random.randint(100000, 999999)+random.random())
		file.write(size + '\n')
		i = i + 1
	file.close()	
