import random
def status_gen():
	file=open('id.txt')#Вместо ID нужно открыть файл, со склееными полями
	ids=file.readlines()
	file.close()	
	status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
	i=0
	file=open('result','w')
	while i<3000:
		res=ids[i]
		a=random.randint(0,12)
		b=len(status[a])
		for x in range(b):		
			file.write(str(res[0:len(res)-1]) + ' ' + status[a][x]+'}'+']'+'\n')
		i=i+1
	file.close()	
