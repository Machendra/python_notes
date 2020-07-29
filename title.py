import os
cols=os.get_terminal_size().columns
given_str=input("Please Enter your title: ")
print (given_str.center(cols))
print (given_str.ljust(cols))
print (given_str.rjust(cols))

