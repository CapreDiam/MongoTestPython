import msgpack

class Serialization:
	def serialization(self,string):
		return msgpack.packb(string)
	def deserialization(self,string):
		return msgpack.unpackb(string)
