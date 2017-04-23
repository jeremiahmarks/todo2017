# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 15:22:45
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-22 18:36:59

class TodoItem(object):
	"""docstring for TodoItem"""
	def __init__(self, idnum, itemName, createdStamp, modifiedStamp):
		super(TodoItem, self).__init__()
		self.itemName = itemName
		self.idnum = idnum
		self.createdStamp = createdStamp
		self.modifiedStamp = modifiedStamp
		self.nameWidth = 80
		self.defautWidth = 20





