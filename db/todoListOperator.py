# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 18:46:11
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-22 18:50:19

import td_db

class todoListOperator(object):
	"""docstring for todoListOperator"""
	def __init__(self):
		super(todoListOperator, self).__init__()
		self.conn, self.cursor = td_db.get_connection_cursor()
		
	def addItemToTodo(self, itemToAdd):
		statement = "INSERT INTO todo_items (description) VALUES (?)"
		self.cursor.execute(statement, (itemToAdd, ))
		self.cursor.connection.commit()
		return self.cursor.lastrowid

	def getTodoItems(self, numberToGet = None):
		if numberToGet is None:
			statement = "SELECT * FROM todo_items"
		elif (0 <= numberToGet): 
			statement = "SELECT * FROM todo_items LIMIT " + str(numberToGet)
		else:
			statement = "SELECT * FROM todo_items"
		self.cursor.execute(statement)
		return self.cursor.fetchall()