import uuid
def generate_save_id():
	i=0
	file = open('id.txt', 'w')
	while i < 3000:
		id=str(uuid.uuid4())
		id=id[0:7] + id[24:32]
		file.write(id + '\n')
		i = i + 1
	file.close()	
