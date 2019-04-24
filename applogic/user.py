from application import db_connect
from application.applogic import  db_queries

def add_user():
	db.cursor.execute(db_queries.add_user)