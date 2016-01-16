import random
DBINSERT=''
DATETIME='datetime.txt'
DIRECTION='direction.txt'
ID='id.txt'
MAGICNUM='magicnum.txt'
PRICE='size.txt'
TAG='tag.txt'
TYPE='types.txt'
CURRENCY='currency.txt'
DURATION='duration.txt'
COMMENT='comment.txt'
COMMENTLEN='comment_length.txt'
TAGLEN='tag_length.txt'
data=''
box=''

def generate_request():
	i = 0
	request_file=  open('request.txt', 'w')
	while i < 3000:
		DBINSERT='db.orders.insert( {  provider: "'	
		if i < 1499 :	
			#FXOpen
			DBINSERT=DBINSERT + '~", '
			DBINSERT=DBINSERT+'id' +': "'+ open_file(ID,i) +'", '
			#concatenate_request("id",box,DBINSERT)
			
			DBINSERT=DBINSERT+'type' +': "'+ open_file(TYPE,i) +'", '
			#concatenate_request("type",box,DBINSERT)
				
			DBINSERT=DBINSERT+'price: ' + str(open_file(PRICE,i)) +', '
			#concatenate_request("price",box,DBINSERT)
			
			DBINSERT=DBINSERT+'direction' +': "'+ open_file(DIRECTION,i) +'", '
			#concatenate_request("direction",box,DBINSERT)
			
			DBINSERT=DBINSERT+'currency' +': "'+ open_file(CURRENCY,i) +'", '
			#concatenate_request("currency",box,DBINSERT)	
			
			DBINSERT=DBINSERT+'duration' +': "'+ open_file(DURATION,i) +'", '
			#concatenate_request("duration",box,DBINSERT) 
			
			DBINSERT=DBINSERT+'comment_length' +': "'+ open_file(COMMENTLEN,i) +'", '
			#concatenate_request("comment_length",box,DBINSERT)
			
			DBINSERT=DBINSERT+'comment' +': "'+ open_file(COMMENT,i) +'", '
			#concatenate_request("comment",box,DBINSERT)
			
			DBINSERT=DBINSERT+'tag_length' +': "'+ open_file(TAGLEN,i) +'", '
			#concatenate_request("tag_length",box,DBINSERT)
			
			DBINSERT=DBINSERT+'tag' +': "'+ open_file(TAG,i) +'", '
			#concatenate_request("tag",box,DBINSERT)	
		else:
			#FXCM
			DBINSERT=DBINSERT + '*", '
			
			DBINSERT=DBINSERT+'id' +': "'+ open_file(ID,i) +'", '
			#concatenate_request("id",box,DBINSERT)
			
			DBINSERT=DBINSERT+'type' +': "'+ open_file(TYPE,i) +'", '
			#concatenate_request("type",box,DBINSERT)
				
			DBINSERT=DBINSERT+'price: ' + str(open_file(PRICE,i)) +', '
			#concatenate_request("price",box,DBINSERT)
			
			DBINSERT=DBINSERT+'direction' +': "'+ open_file(DIRECTION,i) +'", '
			#concatenate_request("direction",box,DBINSERT)
			
			DBINSERT=DBINSERT+'currency' +': "'+ open_file(CURRENCY,i) +'", '
			#concatenate_request("currency",box,DBINSERT)
			DBINSERT=DBINSERT+'desciption' + ': "desciption", '
			#concatenate_request("desciption","desciption",DBINSERT)
		i = i + 1	
		request_file.write(DBINSERT+'\n')
	request_file.close()		
		
def open_file(name,i):
	try:
		file = open(name)
		data=file.readlines()
		file.close()
		box=data[i]
		box=box[0:len(box)-1]
	except IOError as e:
    		print(name + ' - Sorry, could not open file')
	return box 	
def concatenate_request(name_column,text,dbinsert): 
	global DBINSERT
	DBINSERT=DBINSERT+name_column +": "+ text +", "

def price(price,dbinsert):
	global DBINSERT
	DBINSERT=DBINSERT+"price: " + str(price) +", "
