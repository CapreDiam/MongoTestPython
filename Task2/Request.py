import FXCMOrder,FXOpenOrder,random,Serialization,random

fxcm=FXCMOrder.FXCMOrder()
fxopen=FXOpenOrder.FXOpenOrder()
sereliaz=Serialization.Serialization()

class request(FXCMOrder.FXCMOrder,FXOpenOrder.FXOpenOrder,Serialization.Serialization):
    inserts=[]
 
    def insert_request_generation(self):
        queryForFXCM = "db.orders.insert( { "+ "provider: "+'"'+ fxcm.provider() +'"'+ " , id: " + '"'+fxcm.id()+'"'+ " , type: " +'"'+ fxcm.type() + '"'+" , price: " + fxcm.price() + " , direction: " +'"'+ fxcm.direction() +'"'+ " , currency: " + '"'+fxcm.currency() +'"'+ ", decsription: " + '"'+fxcm.decsription()+'"'
        
        queryForFXOpen="db.orders.insert( { "+ "provider: "+ '"'+fxopen.provider() +'"'+ " , id: " +'"'+ fxopen.id()+'"'+ " , type: " +'"'+ fxopen.type() +'"'+ " , price: " + fxopen.price() + " , direction: " +'"'+ fxopen.direction() + '"'+" , currency: " +'"'+ fxopen.currency() + '"'+" , duration: " + '"'+fxopen.duration() +'"'+ " ,  comment_length: " +'"'+ fxopen.comment_length()+'"'+ " , comment: " +'"'+ fxopen.comment() +'"'+ " , tag_length: " +'"'+ fxopen.tag_length() +'"'+ " , tag: " +'"'+fxopen.tag() +'"'+ " , magic_number: " + '"'+fxopen.magicalNumber()+'"'
        a=[queryForFXCM, queryForFXOpen]
        return request().status(a[random.randint(0,1)])
        
        
    def status(self,string):
        status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
        a=random.randint(0,12)
        b=len(status[a])
        for x in range(b):
            dt=fxcm.date_time()
            queryForDB=string+" date: new Date(" + str(dt)+')' + " , status: " + '"' + status[a][x] + '"' + ' }' + ' )'                
            request.inserts.append(queryForDB)
                
        return request.inserts

a=request()        
b=a.insert_request_generation()
print(b)
