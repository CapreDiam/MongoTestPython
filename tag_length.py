import string
import random


def generate_tag_length():
	i=0
	file = open('tag_length.txt', 'w')
	while i < 3000:
		file.write('10' + '\n')
		i = i + 1
	file.close()
