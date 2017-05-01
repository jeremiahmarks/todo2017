# -*- coding: utf-8 -*-
# @Author: Jeremiah
# @Date:   2017-04-19 20:51:58
# @Last Modified by:   Jeremiah Marks
# @Last Modified time: 2017-04-30 19:10:18
# This module will provide various methods to interface with the database. 
#
# There needs to be documentation somewhere, so I am taking the "how about here"
# approach. 
#
# Basically I want to comment on the way that I am using user versions:
# 	Basically I am trying to use them to make the end application something
#	That is highly portable and could skip versions
#	Also it gave me a reason to write those get connection and get cursor methods.
#	I feel like that is somewhere between super ugly and a good idea.


# TODO: use before update trigger to automatically set a last modified marker
# TODO: Explore creating change logs using after update. Useful for determining
#	who keeps making that one change.
# TODO: Create method to ACTUALLY ADD A DAMN TO DO ITEM
import sqlite3

FILE_NAME="tda.sqlite3"
# Per stackoverflow (Yeah, look, it is embarrassing that I said that) 
# this is the best file extension for a sqlite3 file

DB_VERSION=1

# On one hand, writing this just means that I may be able to reduce some code
# If I change this from sqlite3
def get_connection():
	return sqlite3.connect(FILE_NAME)

def get_cursor(connection):
	return connection.cursor()

def get_db_version(cursor):
	cursor.execute("PRAGMA user_version")
	return int(cursor.fetchone()[0])

def get_connection_cursor():
	#Because you need them both to close things.
	connection = get_connection()
	cursor = get_cursor(connection)
	currentDbVersion = get_db_version(cursor)
	# Basically here we are see what version the data base is and then we can 
	# reach appropriately. 

	while currentDbVersion != DB_VERSION:

		if currentDbVersion == 0:
			# If it is currently zero that means that the data base has been created.
			# Our first update is to create the basic todo_items table with its automatic
			# update of the last modified column
			upgradeToOne(cursor)
			cursor.execute("PRAGMA user_version = 1")
		if currentDbVersion == 1:
			# TODO: write this to create the tables needed for tags and projects
			pass


	return connection, cursor

def upgradeToOne(cursor):
	# In case like me, you did not know, sqlite treats
	# any column with the type INTEGER PRIMARY KEY as 
	# an alias to rowid. This means that there is a 
	# potential for primary key reuse, depending on layout.
	# Depending on delete patterns, this could be bad.
	# If you do use AutoIncrement
	# though it will
	triggerStatement = """CREATE TRIGGER update_todoitem_updatetime BEFORE UPDATE ON "todo_items"
	begin
	update "todo_items" set updatetime = strftime('%Y-%m-%d %H:%M:%S:%s','now', 'localtime') where id = old.id;
	end
	"""
	createStatement = """CREATE TABLE "todo_items" ( 
		id INTEGER PRIMARY KEY,
		description text,
		created_date text DEFAULT (strftime('%Y-%m-%d %H:%M:%S:%s','now', 'localtime')),
		updatetime text DEFAULT (strftime('%Y-%m-%d %H:%M:%S:%s','now', 'localtime')))
	"""
	cursor.execute(createStatement)
	cursor.execute(triggerStatement)
	cursor.connection.commit()

def upgradeToTwo(cursor):
	# Where upgradeToOne simply created one database, 
	# version two will include at least two tables, but
	# definitely more. We will need one table for tag names
	# and ids. Also, probably notes. We will need another
	# table to record tag applications. 
	triggerStatement1 = """CREATE TRIGGER delete_tag_applied AFTER DELETE ON "tag_names"
	begin
	DELETE from "tag_applications" WHERE tag_id = old.id;
	end
	"""
	createStatement1 = """CREATE TABLE "tag_names" (
		id INTEGER PRIMARY KEY,
		name TEXT,
		description TEXT);"""
	createStatement2 = """CREATE TABLE "tag_applications" (
		id INTEGER PRIMARY KEY,
		tag_id INTEGER,
		todo_id INTEGER,
		FOREIGN KEY (tag_id) REFERENCES tag_names(id), 
		FOREIGN KEY (todo_id) REFERENCES todo_items(id));"""
	cursor.execute(createStatement1)
	cursor.execute(createStatement2)
	cursor.execute(triggerStatement1)
	cursor.connection.commit()

def revertToOne(cursor):
	# Basically should currently only be used
	# for testing, this creates a way to upgrade
	# to two a second time
	deleteStatement1 = "DROP TABLE tag_names;"
	deleteStatement2 = "DROP TABLE tag_applications;"
	try:
		cursor.execute(deleteStatement1)
	except Exception:
		print (str(Exception))
	try:
		cursor.execute(deleteStatement2)
	except Exception:
		print (str(Exception))
	cursor.connection.commit()
