'''
Created on 04-Apr-2020

@author: HP
'''
#TODO: create a stack
from inspect import stack
stack=[]
#TODO: insert items into stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
#TODO: print the stack
print(stack)
#TODO: find element in a stack
def find(val):
    if val in stack:
        print('value found',val)
    else: 
        print('value not found',val)
#TODO: delete an item
x=stack.pop()
print(x)
print(stack)

find(4)
