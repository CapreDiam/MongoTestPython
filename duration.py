import random
def generate_duration():
	i=0
	file = open('duration.txt', 'w')
	while i < 3000:
		durations = ['Immediate or cancel', 'Good Till Cancel']
		duration = durations[random.randint(0,1)]
		file.write(duration + '\n')
		i = i + 1
	file.close()
