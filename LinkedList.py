'''
Created on 04-Apr-2020

@author: HP
'''
#the Node class
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
    def getData(self):
        return self.val
    
    def setData(self, val):
        self.val = val
        
    def getNext(self):
        return self.next
        
    def setNext(self, next):
        self.next = next
        
#the Linked list 
class LinkedList(object):
    
    def __init__(self,head=None):
        self.head = head
        self.count = 0
        
    def getCount(self):
        return self.count
        
    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        self.count +=1
        
        
    def find(self, val):
        item = self.head
        while (item!= None):
            if item.getData() == val:
                return True
            else: 
                item = item.getNext()
        return None
    
    def deleteAt(self,idx):
        if idx > self.count-1:
            return
        if idx==0:
            self.head = self.head.getNext()
        else:
            tempidx = 0
            node = self.head
            while (tempidx < idx-1):
                node = node.getNext()
                tempidx += 1
            node.setNext(node.getNext().getNext())
            self.count-=1
            
    
    def dumpList(self):
        tempnode= self.head
        while(tempnode != None):
            print('Node:', tempnode.getData())
            tempnode = tempnode.getNext()
        
item_list= LinkedList()
item_list.insert(38)        
item_list.insert(49)        
item_list.insert(13)        
item_list.insert(15)    
item_list.dumpList()    

print('Item count:',item_list.getCount())
print('Finding item:', item_list.find(13))
print('Finding item:', item_list.find(78))


item_list.deleteAt(3)
print('Item count:', item_list.getCount())
print('Finding item:', item_list.find(38))
item_list.dumpList()
        
        