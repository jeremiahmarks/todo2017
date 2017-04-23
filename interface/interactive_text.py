# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 15:22:45
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-22 19:33:12

class TodoItem(object):
	"""docstring for TodoItem"""
	def __init__(self, idnum, itemName, createdStamp, modifiedStamp):
		super(TodoItem, self).__init__()
		self.itemName = itemName
		self.idnum = idnum
		self.createdStamp = createdStamp
		self.modifiedStamp = modifiedStamp
		self.nameWidth = 15
		self.defautWidth = 10

	def __str__(self):
		blockedName = []
		tempname = self.itemName
		while (len(tempname) > 0):
			if len(tempname) <= self.nameWidth:
				while len(tempname) < self.nameWidth:
					tempname += " "
				blockedName.append(tempname[:])
				tempname = ''
			else:
				blockedName.append(tempname[:self.nameWidth])
				tempname =  tempname[self.nameWidth:]
		retstr = "%04d|  " %(self.idnum, )
		retstr = retstr + ''.join(blockedName[0])
		retstr = retstr + "|  " +self.createdStamp
		return retstr

class TodoList(object):
	"""This holds and manages the TodoItems"""
	def __init__(self, dbinterface):
		super(TodoList, self).__init__()
		self.dbinterface = dbinterface
		self.todoItems = []

	def populateItems(self):
		self.todoItems = []
		for eachItem in self.dbinterface.getTodoItems():
			self.todoItems.append(TodoItem(eachItem[0], eachItem[1], eachItem[2], eachItem[3]))

	def printTodoList(self):
		self.populateItems()
		for eachItem in self.todoItems:
			print(eachItem)

	def addTodoItem(self, itemToAdd):
		return self.dbinterface.addItemToTodo(itemToAdd)


		



