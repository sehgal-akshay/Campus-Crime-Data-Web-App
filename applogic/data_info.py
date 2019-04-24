import db_connect as db
from applogic import  db_queries

def get_tuple_count():
	resultSet = []
	aggCount = 0
	tables =['university', 'criminal', 'arrest', 'disciplinary_action', 'vawa', 'hate']
	for table in tables:
		rows = db.cursor.execute(db_queries.tuple_count.format(
				table = table
			)).fetchall()
		count = rows[0][0]
		resultSet.append(count)
	for val in resultSet:
		aggCount += val
	resultSet.append(aggCount) 
	print (resultSet)
	return resultSet