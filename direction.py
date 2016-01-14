import random
def generate_way():
	i=0
	file = open('way.txt', 'w')
	while i < 3000:
		ways = ['sell', 'buy']
		way = ways[random.randint(0,1)]
		file.write(way + '\n')
		i = i + 1
	file.close()	
