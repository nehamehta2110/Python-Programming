'''
Created on 04-Apr-2020

@author: HP
'''
#TODO: create hash table all at once
item = {"key1":1, "key2":2, "key3":3}
print(item)

#TODO: create hash table progressively
item2={}
item2['key1']=1
item2['key2']=2
item2['key3']=3
print(item2)

#TODO: accessing non existent key
#print(item2['key6'])

#TODO: replacing an item
item2['key2']=4
print(item2)

#TODO: iterating through hash table
for key,value in item2.items():
    print('keys:',key,'values:',value)
