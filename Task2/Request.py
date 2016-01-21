import FXCMOrder,FXOpenOrder,random

fxcm=FXCMOrder.FXCMOrder()
fxopen=FXOpenOrder.FXOpenOrder()

class request(FXCMOrder.FXCMOrder,FXOpenOrder.FXOpenOrder):
    
    def insert_request_generation(self):
        queryForFXCM = "db.orders.insert( { "+ "provider: "+'"'+ fxcm.provider() +'"'+ " , id: " + '"'+fxcm.id()+'"'+ " , type: " +'"'+ fxcm.type() + '"'+" , price: " + fxcm.price() + " , direction: " +'"'+ fxcm.direction() +'"'+ " , currency: " + '"'+fxcm.currency() +'"'+ ", decsription: " + '"'+fxcm.decsription()+'"'
        
        queryForFXOpen="db.orders.insert( { "+ "provider: "+ '"'+fxopen.provider() +'"'+ " , id: " +'"'+ fxopen.id()+'"'+ " , type: " +'"'+ fxopen.type() +'"'+ " , price: " + fxopen.price() + " , direction: " +'"'+ fxopen.direction() + '"'+" , currency: " +'"'+ fxopen.currency() + '"'+" , duration: " + '"'+fxopen.duration() +'"'+ " ,  comment_length: " +'"'+ fxopen.comment_length()+'"'+ " , comment: " +'"'+ fxopen.comment() +'"'+ " , tag_length: " +'"'+ fxopen.tag_length() +'"'+ " , tag: " +'"'+fxopen.tag() +'"'+ " , magic_number: " + '"'+fxopen.magicalNumber()+'"'
        
        status = [["New","To Provider","Partially Filled","Filled"],["New", "To Provider", "Filled"],["New","Filled"],["New","Partially Filled","To Provider","Filled"],["New","Partially Filled","To Provider","Rejected","Filled"],["To Provider"],["To Provider","Rejected"],["To Provider","Filled"],["New","To Provider"],["New","To Provider","Rejected"],["New","Partially Filled"],["New"],["New","To Provider","Partially Filled"]]
        i=0
        inserts=[]
        while i<3000:
            i=i+1
            a=random.randint(0,12)
            b=len(status[a])
            for x in range(b):
                dt=fxcm.date_time()
                if i<1499:
                    queryForDB=queryForFXOpen+" date: new Date(" + str(dt)+')' + " , status: " + '"' + status[a][x] + '"' + ' }' + ' )'
                else:
                    queryForDB=queryForFXCM+" date: new Date(" + str(dt)+')' + " , status: " + '"' + status[a][x] + '"' + ' }' + ' )'
                inserts.append(queryForDB)
        return inserts
        
# Посмотреть на запросики        
a=request()
b=a.insert_request_generation()

print(b)
