import sqlite3
from sqlite3 import Error

class AngajatDB(object):
	def __init__(self, db_file):
		""" create a database connection to the SQLite database
			specified by the db_file
		:param db_file: database file
		:return: Connection object or None
		"""
		try:
			self.conn = sqlite3.connect(db_file)
		except Error as e:
			print(e)

 
	def select_all_tasks(self):
		"""
		Query all rows in the tasks table
		:param conn: the Connection object
		:return:
		"""
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM contacts")
	
		rows = cur.fetchall()
	
		for row in rows:
			print(row)
 
 
	def select_all_employees(self):
		"""
		Query tasks by priority
		:param conn: the Connection object
		:param priority:
		:return:
		"""
		cur = self.conn.cursor()
		#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
		cur.execute("SELECT * FROM Angajat")
	
		rows = cur.fetchall()
	
		#for row in rows:
		#    print(row)
		return rows
 
 
