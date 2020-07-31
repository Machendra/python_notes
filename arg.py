'''
import sys
usr_str=input('please enter your string: ')
action=input('please enter your required action lower/upper/title: ')
print (len(sys.argv))
print (sys.argv[0])
if action=='upper':
	print(f' your string in the format {action} is {usr_str.upper()}') 
if action=='lower':
	print(f' your string in the format {action} is {usr_str.lower()}') 
if action=='title':
	print(f' your string in the format {action} is {usr_str.title()}') 
'''
import sys
if len(sys.argv)!=3:
 print (f'please enter in valid format usage: ')
 print(f'{sys.argv[0]}  req_str  upper|lower|title')
 sys.exit(1)
usr_str=sys.argv[1]
action=sys.argv[2]
'''
print (len(sys.argv))
print (sys.argv[0])

'''
if action=='upper':
	print(f' your string in the format {action} is {usr_str.upper()}') 
if action=='lower':
	print(f' your string in the format {action} is {usr_str.lower()}') 
if action=='title':
	print(f' your string in the format {action} is {usr_str.title()}')
else:
 print('you enter in invalid format valid usge is below: ') 
 print(f'{sys.argv[0]}  req_str  upper|lower|title')
