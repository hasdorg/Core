#version : 0.8
import os
import traceback
import json

from os.path import isfile, isdir
from pathlib import Path
from datetime import datetime
from sys import platform

def sysword(): #return hyphen depending system
	if "win" in platform:
		word = "\\"
	else:
		word = "/"
	return word

def syspath(path): #return correct path to object in catalog
	if "win" in platform:
		new_path = f"{Path(__file__).parent}{sysword()}{path}"
		return new_path
	else:
		return path
	
def creator(dirs: dict, catalog: str = Path(__file__).parent): #create dirs
	for dir in dirs:
		path = f"{catalog}{sysword()}{dir}"
		if isdir(path) == False:
			os.mkdir(path)
			
	return True

def easy(list, indent=1):
	dict = json.dumps(list, ensure_ascii=False, indent=indent)
	return dict

empty = ["", " ", "  "]
log_path = syspath(f"logs{sysword()}logs.txt")

class dbjson:
	def __init__(self, filename: str):
		self.filename = filename	

	def login(self, dict: dict = None, range: int = 1):
		def write(path):
			with open(path, 'w', encoding="utf8") as fl:
				if dict:
					fl.write(easy(dict))

		if isfile(self.filename):
			return False
		
		elif isdir(self.filename):
			for r in range(range):
				write(f"{self.filename}{sysword()}{r}.json")

		else:
			if range == 1:
				write(self.filename)

			else:
				for r in range(range):
					write(f"{self.filename}{r}.json")
		return True

	def read(self, varname: str, group=None, address=None):
		if isfile(self.filename):
			with open(self.filename, 'r', encoding="utf8") as fl:
				content = json.loads(fl.read())
				if group == None:
					return content[varname]
				else:
					return content[group][varname]
		else:
			return False
		
	def readdict(self, group=None):
		if isfile(self.filename):
			with open(self.filename, 'r', encoding="utf8") as fl:
				content = json.loads(fl.read())
				if group == None:
					return content
				else:
					return content[group]
		else:
			return False
			
	def write(self, varname: str, value: all):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)

		for file in files:
			if isfile(file) == False:
				dbjson.login(file)

			with open(file, 'r+', encoding="utf8") as fl:
				content = json.loads(fl.read())
				if varname in content.keys():
					content[varname] = value
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
		return True
	
	def append(self, dict_name: str, varname: all, value: all):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)

		for file in files:
			if isfile(file) == False:
				dbjson.login(file)

			with open(file, 'r+', encoding="utf8") as fl:
				content = json.loads(fl.read())
				if dict_name in content:
					new = content[dict_name]
					new[varname] = value
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
		return True
	
	def del_dict(self, dict_name: str, varname: all):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)

		for file in files:
			if isfile(file) == False:
				return False

			with open(file, 'r+', encoding="utf8") as fl:
				content = json.loads(fl.read())
				#dict = content[str(dict)]
				if dict_name in content:
					dict = content[dict_name]
					del dict[varname]
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
		return True
				
	def rename(self, varname: str, newname: str):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)
		
		for file in files:
			with open(file, 'r+', encoding="utf8") as fl:
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
			
	def add(self, varname: str, value: all, position: int = -1):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)
		
		for file in files:
			with open(file, 'r+', encoding="utf8") as fl:
				content = json.loads(fl.read())

				if varname not in content.keys():
					itm = list(content.items())
					key = list(content.keys())
					itm.insert(position, (varname, value))
					content = dict(itm)
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
					
		return True

	def del_var(self, varname: str):
		files = [self.filename] if isfile(self.filename) else os.listdir(self.filename)
		
		for file in files:
			with open(file, 'r+', encoding="utf8") as fl:
				content = json.loads(fl.read())
				
				if varname in content.keys():
					del content[varname]
					fl.seek(0)
					fl.truncate()
					fl.write(easy(content))
					
		return True
		
class logs:
	def __init__(self, path):
		self.path = path
		
	def log_entry(self):
		if isdir(self.path.rpartition(sysword())[0]) == False:
			os.mkdir(self.path.rpartition(sysword())[0])

		error_msg = f"""
	\n
	{datetime.now()}
	{traceback.format_exc()}"""
			
		with open(self.path, 'a', encoding="utf8") as log:
			log.write(error_msg)

		return True
	
	def logs_entry(self, filename, content):
		with open(self.path, 'a', encoding="utf8") as log:
			log.write(f"\n{content}")

	def clear_log(self):
		with open(self.path, 'w', encoding="utf8"):
			return True
		
def access_check(uid, list):
	if uid in list.values():
		return True