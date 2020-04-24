'''
Created on 04-Apr-2020

@author: HP
'''
def fact(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num * fact(num-1)
print("Factorial of {} is {}".format(5,fact(5)))