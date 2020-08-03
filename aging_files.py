import os
import sys
import datetime
req_path=input("Please enter your path: \n ")
age=1
if not os.path.exists(req_path):
	print ("Please provide a valid path ")
	sys.exit(1)
if os.path.isfile(req_path):
	print ("please provide directory path given path contains file")
	sys.exit(2)
today=datetime.datetime.now()
for each_file in os.listdir(req_path):
	each_file_path=os.path.join(req_path,each_file)
	if os.path.isfile(each_file_path):
		file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
		diff_days=(today-file_cre_date).days
		if diff_days>age:
			print(each_file_path,diff_days)
			print(each_file_path)
#script requires additional implementation for deletenig the file
