valid_ver=['2.6','7.8','8.9']
given_ver=input("Please enter your version: ")
if given_ver in valid_ver:
	print(f'given version:{given_ver} is valid')
else:
	print(f'given version:{given_ver} isi not valid')
