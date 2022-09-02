#version : 0.3
import os, sys
import time, random
import json, shutil
import traceback

"""Сделать шаблон, json файл,
который тоже будет редактироваться
при команде rename, add, delete.
Либо отдельный класс, для его пути, и чтобы DB его наследовал,
указать новый класс на нулевом
уровне, ради получения пути к файлу 
шаблона.
"""

from datetime import datetime
from lists import Errors, SystemErrors
from mega import Mega

#m = Mega()
#email = "magicvolgane@gmail.com"
#password = "83637188@herro"
#m.login(email, password)

empty = ['', " ", "  ", "   "]
logs_path = "logs/logs.txt"
lang_path = 'details/lang/'
dbs_path = '/sdcard/Проекты/Telegram/Bots/DataBase'

def easy(list, indent=2):
	pip = json.dumps(list, ensure_ascii=False, indent=indent)
	return pip

class Sample:
	def __init__(self):
		pass

class DB:
	def __init__(self, filename):
		self.filename = filename
		
#	def setup(self):
#		if os.path.isfile(f"{self.filename}"):
#			with open(f"{self.filename}", 'w'):
#				pass
#		else:
#			pass

	def lang(self):
		with open(f"{self.filename}", "r") as fl:
			pass
		#return
		
	def login(self, dict):
		if os.path.isfile(f"{self.filename}.json"):
			return False
		else:
			with open(f"{self.filename}.json", 'w') as fl:
				fl.write(easy(dict))
			return True
			
	def read(self, var):
		with open(f"{self.filename}.json", 'r') as fl:
			content = json.loads(fl.read())
			return content[var]
			
	def write(self, var, value):
		with open(f"{self.filename}.json", "r+") as fl:
			content = json.loads(fl.read())
			if var not in content.keys():
				pass
			else:
				content[var] = value
				fl.seek(0)
				fl.truncate()
				fl.write(easy(content))
				return content[var]
				
	def rename(self, var, name):
		files = os.listdir(f"{self.filename}")
		for r in range(len(files)):
			with open(f"{self.filename}{files[r]}", "r+") as fl:
				r += 1
				content = json.loads(fl.read())
				itm = list(content.items())
				key = list(content.keys())
				itm.insert(key.index(var), (f"{name}", content[var]))
				content = dict(itm)
				del content[var]
				fl.seek(0)
				fl.truncate()
				fl.write(easy(content))
			
	def add(self, var, value, pos=-1):
		files = os.listdir(f"{self.filename}")
		for r in range(len(files)):
			with open(f"{self.filename}{files[r]}", "r+") as fl:
				r += 1
				content = json.loads(fl.read())
				if var in content.keys():
					pass
				else:
					itm = list(content.items())
					key = list(content.keys())
					itm.insert(pos, (f"{var}", f"{value}"))
					content = dict(itm)
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))

	def delete(self, var):
		files = os.listdir(f"{self.filename}")
		for r in range(len(files)):
			with open(f"{self.filename}{files[r]}", "r+") as fl:
				r += 1
				content = json.loads(fl.read())
				del content[var]
				fl.seek(0)
				fl.truncate()
				fl.write(easy(content))

#class DBChat(DB):
#	def __init__(self, filename):
#		self.filename = filename
		
def access_check(uid, list1):
	if uid in list1.values():
		return True
	else:
		return False
	
#	if list2 == None:
#		if uid in list1:
#			return True
#		else:
#			return False
#	elif list2 != None:
#		if uid in list1 or uid in list2:
#			return True
#		else:
#			return False
#	else:
#		log_entry(SystemErrors.func_error + "acess_check")
		
def log_entry(comment="", path=logs_path):
	if os.path.isdir(path.rpartition("/")[0]) == False:
		os.mkdir(path.rpartition("/")[0])
		
	if comment != "":
		error_msg = f"""
\n
{datetime.now()}
{comment}
{traceback.format_exc()}"""

	else:
		error_msg = f"""
\n
{datetime.now()}
{traceback.format_exc()}"""
		
	with open(path, 'a') as log:
		log.write(error_msg)
		
def clear_log(path=logs_path):
	try:
		with open(path, 'w'):
		   pass
	except Exception:
	   log_entry(SystemErrors.func_error +"«clear_log»")
	   
def db_reserve():
	try:
		shutil.copytree(dbs_path, '/sdcard/Проекты/TelegramBots/Archive/DataBases/')
	except Exception:
	   log_entry(SystemErrors.func_error +"«clear_log»")
	   
def check_language(path, uid):
	try:
		pass
	except Exception:
	   log_entry(SystemErrors.func_error +"«clear_log»")
	   
#db = DB("/sdcard/Download/test/test.json")