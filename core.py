#version : 0.65
import os, sys
import shutil
import traceback
import time
import random
import json
#import pymongo
#import sqlite3

from os.path import isfile, isdir
from datetime import datetime

empty = ["", " "]
log_path = "logs/logs.txt"

def easy(list, indent=1):
	dict = json.dumps(list, ensure_ascii=False, indent=indent)
	return dict

#class Sample:
#	def __init__(self, filename):
#		pass

class dbjson:
#	def __new__():
	def __init__(self, filename: str):
		self.filename = filename
		
#	def setup(self):
#		if os.path.isfile(f"{self.filename}"):
#			with open(f"{self.filename}", 'w'):
#				pass
#		else:
#			pass
		
	def login(self, dict: dict):
		if isfile(self.filename):
			return False
		else:
			with open(self.filename, 'w') as fl:
				fl.write(easy(dict))
			return True
			
	def read(self, varname: str, group=None):
		with open(self.filename, 'r') as fl:
			content = json.loads(fl.read())
			if group == None:
				return content[varname]
			else:
				return content[group][varname]
			
	def write(self, varname: str, value: all):
		with open(self.filename, 'r+') as fl:
			content = json.loads(fl.read())
			if varname not in content.keys():
				return False
				
			else:
				content[varname] = value
				fl.seek(0)
				fl.truncate()
				fl.write(easy(content))
				return True
				
	def rename(self, varname: str, newname: str):
		files = [self.filename] if isfile(self.filename) else os.listdir(filename)
		
		for file in files:
			with open(file, 'r+') as fl:
				content = json.loads(fl.read())
				itm = list(content.items())
				key = list(content.keys())
				itm.insert(key.index(varname), (newname, content[varname]))
				content = dict(itm)
				del content[varname]
				fl.seek(0)
				fl.truncate()
				fl.write(easy(content))
				
		return True
			
	def add(self, var: str, value: all, position: int =-1):
		files = [self.filename] if isfile(self.filename) else os.listdir(filename)
		
		for file in files:
			with open(file, 'r+') as fl:
				content = json.loads(fl.read())

				if var in content.keys():
					pass
					
				else:
					itm = list(content.items())
					key = list(content.keys())
					itm.insert(position, (var, value))
					content = dict(itm)
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
					
		return True

	def delete(self, varname: str):
		files = [self.filename] if isfile(self.filename) else os.listdir(filename)
		
		for file in files:
			with open(file, 'r+') as fl:
				content = json.loads(fl.read())
				
				if varname in content.keys():
					del content[varname]
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
					
				else:
					continue
					
		return True
		
class dbmongo:
	def __init__(self, filename: str):
		pass
				
class dbsqlite3:
	def __init__(self, filename: str):
		self.con = sqlite3.connect(filename)
		self.cur = con.cursor()
		self.filename = filename
		
	def read(self, var):
		pass
		
	def write(self, varname, value):
		pass
	
	def add(self, var, value, pos):
		pass
		
	def rename(self, var, newname):
		pass
		
	def delete(self, varname):
		pass
		
def access_check(uid, list):
	if uid in list.values():
		return True
	else:
		return False
		
def log_entry(comment=None, path=log_path):
	if isdir(path.rpartition("/")[0]) == False:
		os.mkdir(path.rpartition("/")[0])
		
	if comment != None:
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
		
	return True
		
def clear_log(path=log_path):
	try:
		with open(path, 'w'):
			pass
			
		return True
	except Exception:
	   log_entry("Func Error: clear_log")
	   return False