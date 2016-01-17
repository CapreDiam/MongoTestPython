import subprocess
import commands

def insert_query():
        statuses = ["New", "To Provider", "Partially Filled","Filled","Rejected"]
        count=len(statuses)
        i=0
        file = open('Test/querys','w')
        for i in range(count):
                quer1=status_by_id(str(statuses[i]))#Count id by every status
                file.write(quer1+'\n')
        file.write( "db.orders.aggregate( [ { $match : { provider: "+'"'+'*'+'"'+" } }, { $group: { _id: "+'"'+"$provider"+'"'+", sum: { $sum: "+'"'+"$price"+'"'+" } } } ] )"+'\n')#Count sum by "*" provider
        file.write( "db.orders.aggregate( [ { $match : { provider: "+'"'+'~'+'"'+" } }, { $group: { _id: "+'"'+"$provider"+'"'+", sum: { $sum: "+'"'+"$price"+'"'+" } } } ] )"+'\n')#Count sum by "~" provider
	file.write("db.orders.aggregate( { $group: { _id: "+'"'+"$id"+'"'+", count: { $sum: 1 } } }, { $sort: { _id: 1 } }, { $limit: 3 } )"+'\n')#Count id by every status(only for 3 orders) 
	file.write("db.orders.aggregate( [ { $match : { date: { $gte: new Date("+'"'+"2016"+'\\'+"1"+'\\'+"15 9:12:24.25"+'"'+"),$lte: new Date("+'"'+"2016"+'\\'+"1"+'\\'+"15 9:12:24.725"+'"'+ ") } } }, { $group: { _id: null, count: { $sum: 1 } } } ] )"+'\n')#Count orders between 2 dates

        file.close()
        

def write_reslut():
        file = open('Test/querys')
       	buff=file.readlines()
     	i=0
    	f = open ('Test/results','w')
	operation = "mongo < querys"
	result = commands.getoutput(operation)
	f.write(result[50:len(result)-3])   
	f.close()     

def status_by_id(status):
                query="db.orders.find( { status: "+'"'+status+'"'+ " } ).count()"
                return query

insert_query()
write_reslut()
