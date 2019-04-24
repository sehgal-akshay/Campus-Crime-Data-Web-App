import db_connect as db
from applogic import  db_queries

def validate_login(email, password):
	resultSet = [];
	print("hello")
	print(email)
	print(password)
	rows = db.cursor.execute(db_queries.validate_login.format(
                email=email,
                password=password)).fetchall()
	if(rows):
		resultSet.append(rows)
		return resultSet	
	else:
		return None

def register_user(username, email, password):
	print('here')
	print(username)
	#db.cursor.execute("INSERT INTO users (username, email, password) VALUES" (username, email, password))
	db.cursor.execute("""INSERT INTO users VALUES(:1,:2,:3)""", {
		"1":username,
		"2":email,
		"3":password
		})
	db.connection.commit()
	