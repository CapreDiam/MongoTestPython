import json
from datetime import datetime, date, time
from decimal import *

def result_tests_data():
	sum_id_new=0
	sum_id_to_provider=0
	sum_id_reject=0
	sum_id_field=0
	sum_id_partially_field=0
	sum_price_for_fxopen=0
	sum_price_for_fxcm=0
	sum_id_orders_1=0
	sum_id_orders_2=0
	sum_id_orders_3=0
	sum_beetwen_date=0
	dtfirst = datetime.strptime('2016/1/15 9:12:24.25', '%Y/%m/%d %H:%M:%S.%f')
	dtsecond = datetime.strptime('2016/1/15 9:12:24.725', '%Y/%m/%d %H:%M:%S.%f')	
	
	id_file=open('Tests/results.txt')
	_id=id_file.readlines()
	id_first=_id[7]
	id_first=id_first[11:len(id_first)-17]
	id_second=_id[8]
	id_second=id_second[11:len(id_second)-17]
	id_third=_id[9]
	id_third=id_third[11:len(id_third)-17]

	file=open('jsondatafile.txt')
	json_file=file.readlines()
	size = len(json_file)
	file.close()
	for each in range(size):
		buff=json_file[each]
		json_string = json.loads(buff[0:len(json_file[each])-1])
		#Sum count each status
		if json_string["status"]=="New":
			sum_id_new=sum_id_new+1
		elif json_string["status"]=="To Provider":
			sum_id_to_provider=sum_id_to_provider+1
		elif json_string["status"]=="Partially Filled":
			sum_id_partially_field=sum_id_partially_field+1
		elif json_string["status"]=="Filled":
			sum_id_field=sum_id_field+1
		else: 
			sum_id_reject=sum_id_reject+1
		#sum price for each provider
		if json_string["provider"]=="*":
			sum_price_for_fxcm=sum_price_for_fxcm+float(json_string["price"])
		else:
			sum_price_for_fxopen=sum_price_for_fxopen+float(json_string["price"])
		#count id, status order
		if json_string["id"]==id_first:
			sum_id_orders_1=sum_id_orders_1+1
		elif json_string["id"]==id_second:
			sum_id_orders_2=sum_id_orders_2+1
		elif json_string["id"]==id_third:
			sum_id_orders_3=sum_id_orders_3+1
		#sum price between 2 date
		buff_date=datetime.strptime(json_string["date"], '%Y.%m.%d %H:%M:%S.%f')
		if buff_date>=dtfirst and buff_date<=dtsecond:
			sum_beetwen_date=sum_beetwen_date+1
	file=open('Tests/jsondatafileresult.txt','w')
	file.write(str(sum_id_new)+'\n')
	file.write(str(sum_id_to_provider)+'\n')
	file.write(str(sum_id_partially_field)+'\n')
	file.write(str(sum_id_field)+'\n')
	file.write(str(sum_id_reject)+'\n')
	file.write('{ "_id" : "*", "sum" : ' + str(sum_price_for_fxcm) + ' }'+'\n')
	file.write('{ "_id" : "~", "sum" : ' + str(sum_price_for_fxopen) + ' }'+'\n')
	file.write('{ "_id" : "'+id_first + '", "count" : ' + str(sum_id_orders_1) + ' }'+'\n')
	file.write('{ "_id" : "'+id_second +'", "count" : ' + str(sum_id_orders_2) + ' }'+'\n')
	file.write('{ "_id" : "'+id_third +'", "count" : ' + str(sum_id_orders_3) + ' }'+'\n')
	file.write('{ "_id" : null, "count" : ' + str(sum_beetwen_date) + ' }'+'\n')
