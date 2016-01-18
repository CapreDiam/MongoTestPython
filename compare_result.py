import commands
def copmares_results():
	try:
		mongo_file=open('Tests/results.txt','r')
		python_calculat=open('Tests/jsondatafileresult.txt','r')
		report_passed_test=open('Tests/report_passed_test.html','w')
		result_mongo=mongo_file.readlines()
		result_python=python_calculat.readlines()
		size=len(result_mongo)
		for index in range(size):
			print("|-----------------|")
			python=result_python[index]
			mongo=result_mongo[index]
			python=python[0:len(python)-1]
			mongo=mongo[0:len(mongo)-1]
			if index==5 or index==6:
				python=round(float(python[23:len(python)-2]),2)
				mongo=round(float(mongo[23:len(mongo)-2]),2)
			md5_python=commands.getoutput("echo -n " + str(python) + " | md5sum")
			md5_mongo=commands.getoutput("echo -n " + str(mongo) + " | md5sum")
			if md5_python==md5_mongo:
				print '|Test [',str(index+1), '] passed|'
			else:
				print '|Test [', str(index+1),'] wrong |'
			print("|-----------------|")	
	except IOError as e:
    		print(str(e)+ ' - Sorry, could not open file')
	mongo_file.close()
	python_calculat.close()
	report_passed_test.close()
