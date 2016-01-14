import string
import random

def randstring():
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(10)])


def generate_tag():
	i=0
	file = open('tag.txt', 'w')
	while i < 3000:
		tag=randstring()
		file.write(tag + '\n')
		i = i + 1
	file.close()
