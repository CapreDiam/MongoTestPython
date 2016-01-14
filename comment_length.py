import string
import random

def generate_comment_length():
	i=0
	file = open ('comment_length', 'w')	
	while i < 3000:
		file.write('30' + '\n')		
		i = i + 1
	file.close()
