'''
Created on 04-Apr-2020

@author: HP
'''
def countdown(num):
    if num == 0:
        print('..Done!')
    else:
        print(num,'..')
        countdown(num-1)
countdown(5)        