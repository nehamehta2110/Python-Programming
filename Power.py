'''
Created on 04-Apr-2020

@author: HP
'''
def power(num,pow):
    if pow==0:
        return 1
    else:
        return num * power(num,pow-1)
    
print("{} raised to the power {} is {}".format(5,3,power(5,3)))
print("{} raised to the power {} is {}".format(2,3,power(2,3)))