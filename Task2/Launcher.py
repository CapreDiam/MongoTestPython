from Result import Result

request = Result()

request.insert_request("db.orders.remove({})")
request.generation_request_insert()
request.result_data()
