import random
def generate_direction():
	i=0
	file = open('direction.txt', 'w')
	while i < 3000:
		directions = ['sell', 'buy']
		direction = directions[random.randint(0,1)]
		file.write(direction + '\n')
		i = i + 1
	file.close()	
