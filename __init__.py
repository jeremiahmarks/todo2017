# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 19:04:12
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-22 19:31:08

from db import todoListOperator
from interface import interactive_text

thisOperator = todoListOperator.todoListOperator()
todolist = interactive_text.TodoList(thisOperator)

def test():
	todolist.addTodoItem("This is test item #1!")
	todolist.addTodoItem("This is another test item!")
	todolist.printTodoList()

if __name__ == '__main__':
	test()