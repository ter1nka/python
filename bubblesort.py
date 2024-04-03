#!/usr/bin/env python3

def simple(seznam):
    for i in range(len(seznam)):
        for j in range(len(seznam) - i - 1):
            if seznam[j] > seznam[j+1]:
                temp = seznam[j]
                seznam[j] = seznam[j+1]
                seznam[j+1] = temp 
    return seznam
    
if __name__== '__main__':
    seznam = [-2, 45, 0 ,11 , -9, 10]
    print(simple(seznam))