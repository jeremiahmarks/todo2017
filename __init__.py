# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-22 19:04:12
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-22 19:16:46

from db import todoListOperator
from interface import interactive_text

thisOperator = todoListOperator.todoListOperator()
todolist = interactive_text.TodoList(thisOperator)
