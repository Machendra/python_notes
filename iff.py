num=eval(input("please enter your number: "))
print(f'you enterd number {num}')
print(f'you enterd number type {type(num)}') 
'''
if num==1:
    print ("one")
if num==2:
    print ("two")
if num==3:
    print ("three")
if num==4:
    print ("four")
else:
   print(f'entered num {num} is out of range please enter b/w 1-4')
'''
num_value={1:'one',2:'two',3:'three',4:'four'}
if num in [1,2,3,4]:
   print(num_value.get(num))
else:
   print(f'entered num {num} is out of range please enter b/w 1-4')
