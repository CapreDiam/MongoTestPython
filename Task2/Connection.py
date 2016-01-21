import pymongo
class connection:
    def connect():
        conn = pymongo.Connection('localhost', 27017)
        db = conn['db']
        coll=db['orders']
