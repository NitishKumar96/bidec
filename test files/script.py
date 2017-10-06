#!/usr/local/bin/python

# script to search for the functions with no comments

import os
import linecache as File
#//////////////////////////////////////////////// all the functions

# function to detect that it is a valid function
def  phpCheckfn(line_list):
	if line_list[0] == "function" :
		# print line_list
		# functionName= line_list[1].split("(")[0]
		# print functionName
		return True	
	else:
		return False

def phpCheckfncomments(lineNo):
	line=File.getline(current_file,lineNo)
	line_list=line.split()
	functionName=line_list[1].split("(")[0]
	# print str(lineNo) +"	"+functionName

	error.append("function name: "+ functionName)
	error.append("line no.: "+ str(lineNo))
	
	comment=False
	discription=False
	i= lineNo
	j= lineNo
	while i >0:
		i= i-1
		com_line = File.getline(current_file,i)

		if len(com_line.split())>0:
			if "//"== com_line.split()[0] or "*/" in com_line or comment==True :
				comment=True
				if functionName in  com_line:
					discription=True
				else:
					discription=False

				if "//"== com_line.split()[0] or "/*"== com_line.split()[0]:
					comment=False
			else:
				break
			
	if comment== False and discription==True:
		comment= False
	else:
		error.append("Improper discription ; "+"\""+ line.strip()+"\"" + " --> error: " + err_11)
		# line.split() ==> to remove \n from the end of the line
		

	if "{" in line:
		error.append("Bad format ; "+"\""+ line.strip()+"\"" + " --> error: " + err_21)
	
	return


#///////////////////////////////////////////////// all variables
search_folder='.'
dir_names=["test files"]   # "css","application","js"
check_line=True
Lcm=False
Bcm=False
isFn= False
inPHP=False
errors=[]					# list of all the errors
error=[]					# temp list of error
# html_files=[]				# list of html files and there add
php_files=[]				# list of names of php files
# python_files=[]
types=[]					# list of file type encountered
#.................
#following are the list of the error massage
err_11="function discription not present "
err_21=" '{' should come in the next line"


#////////////////////////////////////////////////// final code

os.system('clear') 					 # clears the terminal screen before printing

for root, dirs, files in os.walk(search_folder):
	if root.split("/")[-1] in dir_names:
		# print "\n!--- "+root
		# print dirs+files

		for root1, dirs1 , files1 in os.walk(root):
			# print root1
			# print dirs1
			# print files1

			if len(dirs1) != 0 :
				for name1 in dirs1:
					for file1 in files1:
						file_type1= file1.split(".")[-1]
						# code to short the file with there file type
						if file_type1=='php':
				 			php_files.append([file1,os.path.join(root,file1)])

				 		if not file_type1 in types:
							types.append(file_type1)


 			else:
 				for file1 in files1:
					file_type1= file1.split(".")[-1]
					# code to short the file with there file type
					if file_type1=='php':
			 			php_files.append([file1,os.path.join(root,file1)])

			 		if not file_type1 in types:
							types.append(file_type1)

lineNo=0
y=0
current_file= php_files[0][1]

# a simple loop to see the full file
# with open(current_file) as f:
# 	data = f
# 	print data.read()
	

# print "...................................."   # a seperator

# to short the functions

print types

with open(current_file) as f:					# open the file
	for line in f:								# take one line at a time
		Lcm=False								# assume that it is not a comment
		lineNo+=1 								# take the line number
		splitline=line.split()					# make a list of elements
		
		if len(splitline) >0:					# check line is empty or not
			if splitline[0]== "//":
				Lcm=True
			elif splitline[0]=="/*":
				Bcm=True
			elif splitline[0]== "*/":
				Bcm=False
			
			if line.split()[0] in ["<?php","<?PHP"]:
				inPHP=True
			elif line.split()[0] == "?>":
				inPHP=False

			if Lcm== False and Bcm== False and inPHP==True:    		# line is not comment
				if "function" in line :
					isFn= phpCheckfn(line.split())

					if isFn:
						phpCheckfncomments(lineNo)


if len(error)>2:
	for err in error:
		print err
else:
	print" no errors with function"

