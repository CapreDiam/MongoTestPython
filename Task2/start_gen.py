import Data_generating

path=Data_generating.generation()
	

def inputdata():
		
		
                file = open('examlpe','w')#ЧИСТО ДЛЯ ПРОСМОТРА
		
                for i in range(3000):
			DBINSERT='db.orders.insert( {  provider: "'
			if i < 1499 :	
				#FXOpen
				DBINSERT=DBINSERT + '~", '
				DBINSERT=DBINSERT+'id' +': "'+ path.id() +'", '
				DBINSERT=DBINSERT+'type' +': "'+ path.type() +'", '
				DBINSERT=DBINSERT+'price: ' + str(path.size()) +', '
				DBINSERT=DBINSERT+'direction' +': "'+ path.direction() +'", '
				DBINSERT=DBINSERT+'currency' +': "'+ path.currency() +'", '
				DBINSERT=DBINSERT+'duration' +': "'+ path.duration() +'", '
				DBINSERT=DBINSERT+'comment_length' +': "'+ path.lencom() +'", '
				DBINSERT=DBINSERT+'comment' +': "'+ path.comment() +'", '
				DBINSERT=DBINSERT+'tag_length' +': "'+ path.lentag() +'", '
				DBINSERT=DBINSERT+'tag' +': "'+ path.tag() +'",'
			else:
				#FXCM
				DBINSERT=DBINSERT + '*", '			
				DBINSERT=DBINSERT+'id' +': "'+ path.id() +'", '		
				DBINSERT=DBINSERT+'type' +': "'+ path.type() +'", '
				DBINSERT=DBINSERT+'price: ' + str(path.size()) +', '
				DBINSERT=DBINSERT+'direction' +': "'+ path.direction() +'", '
				DBINSERT=DBINSERT+'currency' +': "'+ path.currency() +'", '
			
               		file.write(DBINSERT+'\n')
                file.close()
inputdata()