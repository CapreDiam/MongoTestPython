import commands
def clear_db():
	file =open('clears.txt','w')
	file.write("db.orders.remove({})")
	file.close()
	res="mongo < clears.txt"
	comand=commands.getoutput(res)
	file=open('log.txt','w')
	file.write(comand)
	file.close()
