import string
import random

def randstring():
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(30)])


def generate_comment():
	i=0
	file = open('comment.txt', 'w')
	while i < 3000:
		comment=randstring()
		file.write(comment + '\n')
		i = i + 1
	file.close()
