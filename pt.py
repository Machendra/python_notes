import getpass
dbpaswd=getpass.getpass(prompt="please enter your DB password: ")
print (f'your DB password is {dbpaswd}')
username=getpass.getuser()
print (f'your username is {username}')
