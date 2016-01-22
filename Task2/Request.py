import FXCMOrder,FXOpenOrder,random,Serialization,random,commands

fxcm=FXCMOrder.FXCMOrder()
fxopen=FXOpenOrder.FXOpenOrder()
sereliaz=Serialization.Serialization()

class request(FXCMOrder.FXCMOrder,FXOpenOrder.FXOpenOrder,Serialization.Serialization):
    results_db=[]
    results_python=[]
    
    def insert_request_generation(self):
        queryForFXCM = "db.orders.insert( { "+ "provider: "+'"'+ fxcm.provider() +'"'+ " , id: " + '"'+fxcm.id()+'"'+ " , type: " +'"'+ fxcm.type() + '"'+" , price: " + fxcm.price() + " , direction: " +'"'+ fxcm.direction() +'"'+ " , currency: " + '"'+fxcm.currency() +'"'+ ", decsription: " + '"'+fxcm.decsription()+'" ,'
        
        queryForFXOpen="db.orders.insert( { "+ "provider: "+ '"'+fxopen.provider() +'"'+ " , id: " +'"'+ fxopen.id()+'"'+ " , type: " +'"'+ fxopen.type() +'"'+ " , price: " + fxopen.price() + " , direction: " +'"'+ fxopen.direction() + '"'+" , currency: " +'"'+ fxopen.currency() + '"'+" , duration: " + '"'+fxopen.duration() +'"'+ " ,  comment_length: " +'"'+ fxopen.comment_length()+'"'+ " , comment: " +'"'+ fxopen.comment() +'"'+ " , tag_length: " +'"'+ fxopen.tag_length() +'"'+ " , tag: " +'"'+fxopen.tag() +'"'+ " , magic_number: " + '"'+fxopen.magicalNumber()+'" ,'
        a=[queryForFXCM, queryForFXOpen]
        b=random.randint(0,1)
        c=a[b]
        return request().status(c)
        
        
    def status(self,string):
        status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
        a=random.randint(0,12)
        b=len(status[a])
        for x in range(b):
            dt=fxcm.date_time()
            queryForDB=string+" date: new Date(" + str(dt)+')' + " , status: " + '"' + status[a][x] + '"' + ' }' + ' )' 
            operation = '"' +"mongo < "+queryForDB+'"'
            #print(queryForDB)
            commands.getoutput(operation)      
               
        
    def request_db(self):
        request().id_by_status()
        request().sum_by_fxcm()   
        request().sum_by_fxopen()
        request().status_by_id()
            
    def id_by_status(self):
        statuses = ["New", "To Provider", "Partially Filled","Filled","Rejected"]
        for i in range(len(statuses)):
            query1= "db.orders.find( { status: "+'"'+statuses[i]+'"'+ " } ).count()"
            operation = '"' +"mongo < "+query1+'"'
            request.results_db.append(commands.getoutput(operation))  
            
    def sum_by_fxcm(self):
        query2="db.orders.aggregate( [ { $match : { provider: "+'"'+'*'+'"'+" } }, { $group: { _id: "+'"'+"$provider"+'"'+", sum: { $sum: "+'"'+"$price"+'"'+" } } } ] )" 
        operation = '"' +"mongo < "+query2+'"'
        request.results_db.append(commands.getoutput(operation))
            
    def sum_by_fxopen(self):
        query2="db.orders.aggregate( [ { $match : { provider: "+'"'+'~'+'"'+" } }, { $group: { _id: "+'"'+"$provider"+'"'+", sum: { $sum: "+'"'+"$price"+'"'+" } } } ] )"
        operation = '"' +"mongo < "+query2+'"'
        request.results_db.append(commands.getoutput(operation))
    
    def status_by_id(self):
        query3="db.orders.aggregate( { $group: { _id: "+'"'+"$id"+'"'+", count: { $sum: 1 } } }, { $limit: 3 } )"
        operation = '"' +"mongo < "+query3+'"'
        request.results_db.append(commands.getoutput(operation))    
        
    def between_dates(self):
        query4="db.orders.aggregate( [ { $match : { date: { $gte: new Date("+'"'+"2016"+'\\'+"1"+'\\'+"15 9:12:24.25"+'"'+"),$lte: new Date("+'"'+"2016"+'\\'+"1"+'\\'+"15 9:12:24.725"+'"'+ ") } } }, { $group: { _id: null, count: { $sum: 1 } } } ] )"
        operation = '"' +"mongo < "+query4+'"'
        request.results_db.append(commands.getoutput(operation))     
    
    def insert_request(self):
        a=request()
        b=0
        while b < 3000:
             a.insert_request_generation()
             b=b+1           

mongo=request()
mongo.insert_request()
mongo.request_db()
