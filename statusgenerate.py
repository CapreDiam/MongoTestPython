import random
def status_gen():
	file=open('request.txt')
	json_file=open('jsondatafile.txt')
	jsf=json_file.readlines()
	ids=file.readlines()
	file=open('datetime.txt')
	datetime=file.readlines()
	file.close()
	json_file.close()	
	status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
	i=0
	json_file=open('jsondatafile.txt','w')
	file=open('request_final.txt','w')
	counter_datetime=0;
	while i<3000:
		res=ids[i]
		resj=jsf[i]
		a=random.randint(0,12)
		b=len(status[a])
		for x in range(b):
			dt=datetime[counter_datetime]		
			file.write(str(res[0:len(res)-1]) + " date: new Date(" +str(dt[0:len(dt)-1])+'), ' + "status: "+ '"'+status[a][x]+'"'+'}'+')'+'\n')
			json_file.write(str(resj[0:len(resj)-1]) + ' "date":' +str(dt[0:5])+"." + str(dt[6])+ "."+str(dt[8:len(dt)-1])+', ' + '"status": '+ '"'+status[a][x]+'"'+'}'+'\n')
			counter_datetime=counter_datetime+1
		i=i+1
		
	file.close()
	json_file.close()	
