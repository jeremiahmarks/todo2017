# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 18:46:11
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-30 20:45:09

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

	def getTodoByTag(self, tagId):
		statement = "SELECT * FROM tag_applications JOIN todo_items ON tag_applications.todo_id = todo_items.id WHERE tag_applications.tag_id = ?"
		self.cursor.execute(statement, (tagId, ))
		return self.cursor.fetchall()


	def addTag(self, tagName):
		statement = "INSERT INTO tag_names (name) VALUES (?);"
		self.cursor.execute(statement, (tagName, ))
		self.cursor.connection.commit()
		return self.cursor.lastrowid

	def applyTag(self, todoId, tagId):
		statement = "INSERT INTO tag_applications (tag_id, todo_id) VALUES (?, ?);"
		self.cursor.execute(statement, (tagId, todoId))
		self.cursor.connection.commit()
		return self.cursor.lastrowid

	def removeTag(self, todoId, tagId):
		statement = "DELETE FROM tag_applications WHERE todo_id = ? AND tag_id = ?"
		self.cursor.execute(statement, (todoId, tagId))
		self.cursor.connection.commit()
		return True

	def deleteTag(self, tagId):
		# This one tests my ability to write the 
		# trigger statement correctly. Fingers
		# crossed
		statement = "DELETE FROM tag_names WHERE id = ?"
		self.cursor.execute(statement, (tagId, ))
		self.cursor.connection.commit()
		return True

