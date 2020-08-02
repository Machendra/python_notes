import os
req_path=input("please enter your dir path: ")
if os.path.isfile(req_path):
	print(f'the given path is file please enter a valid path of dir: ')
else:
	all_f_dir=os.listdir(req_path)
	if all_f_dir==0:
		print(f'there are no files in the {req_path} please choose another dir')
	else:
		req_ex=input('please enter required extension .sh .py .txt')
		req_files=[]
		for each_f in all_f_dir:
			if each_f.endswith(req_ex):
				req_files.append(each_f)

		if len(req_files)==0:
			print (f'please enter valid extensions there are no files ending with {req_ex} ')
		else: 
			print(f'there are {len(req_files)} in the {req_path} ')
			print(f'so the files are: {req_files} ' )
