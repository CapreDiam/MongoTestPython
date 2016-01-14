import random
def generate_magic_num():
	i=0
	file = open('magic_num.txt', 'w')
	while i < 3000:
		number = str(random.randint(100000, 999999))
		file.write(number + '\n')
		i = i + 1
	file.close()	
