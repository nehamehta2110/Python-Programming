'''
Created on 04-Apr-2020

@author: HP
'''
def gcd(a,b):
    while (b!=0):
        t=a
        a=b
        b=t%b
        
    return a
print(gcd(20, 8))