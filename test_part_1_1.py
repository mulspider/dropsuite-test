import os
import sqlite3
from sqlite3 import Error

db_file = './counter.db'
conn = None
try:
	tcounter = ''' CREATE TABLE  IF NOT EXISTS  tcontent (contents TEXT) '''
	conn = sqlite3.connect(db_file)
	cur = conn.cursor()
	cur.execute(tcounter)
	conn.commit()
	tdeltable = '''DELETE FROM tcontent'''
	cur.execute(tdeltable)
	conn.commit()

	path = input("Enter your specific path: ")
	# ext = input("Enter your specific ext file: ")

	def readFile(filename):
		data = ''
		with open(filename, 'r') as file:
			data = file.read()
		return data

	isdir = os.path.isdir(path) 
	if isdir:
		pathname = os.path.abspath(path)
		# print(pathname)
		if isdir:
			listfile = os.listdir(path)

		length = len(listfile)

		for i in range(length):
			files = pathname+"\\"+listfile[i]
			isFile = os.path.isfile(files) 
			# print(isFile)
			if isFile:
				cont = readFile(files)
				if cont != None:
					try:
						xsql = ''' insert into tcontent (contents) values ('%s')  '''% (cont)
						cur.execute(xsql)
						conn.commit()
					except:
						None

		xselect = ''' select contents, max(counts) from (select contents, count(contents) as counts from tcontent group by contents) '''
		cur.execute(xselect)
		lx = cur.fetchall()
		for n in lx:
			print("content : " + n[0] + " has " + str(n[1]) + " files")
		

except Error as e:
        print(e)
finally:
  if conn:
     conn.close()
