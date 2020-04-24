'''
Created on 04-Apr-2020

@author: HP
'''
from collections import deque

#TODO: CREATE A QUEUE
queue = deque()

#TODO: INSERT ITEMS IN QUEUE
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#TODO: PRINT ITEMS IN QUEUE
print(queue)

#TODO: find element in a queue
def find(val):
    if val in queue:
        print('value found',val)
    else: 
        print('value not found',val)

#TODO: REMOVE AN ITEM (first in first out)
x= queue.popleft()
print(x)
print(queue)

find(3)
find(1)
