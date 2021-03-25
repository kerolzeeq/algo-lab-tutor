# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:15:00 2021

@author: Khairol Hazeeq
"""
def rabinkarp(string,pattern,d_ascii):
    m=len(string)
    n=len(pattern)
    hashpat=0
    hashgroup=0
    power=n-1
    #kira hash value of pattern and first group
    for i in range(n):
        hashpat=hashpat+(ord(pattern[i])*d_ascii**power) # 97x256^2 + 90x256^1
        hashgroup=hashgroup+(ord(string[i])*d_ascii**power)
        power-=1

    #move group next 123 - 232
    for i in range(m):
            check=0
            if(hashpat==hashgroup): #check each alphabet
                for j in range(n):
                    if string[i+j]!=pattern[j]:
                        break
                    else: check+=1
                if check==n:
                    print(pattern," found at ",i)
            if(i<m-n):
                 hashgroup=(hashgroup-ord(string[i])*d_ascii**2)*d_ascii  + ord(string[i+n])
        
    


#string = input("Enter string : ")
string="afunpafunnyfnulgfunoisfun"
pattern = "fun"

d_ascii=256

rabinkarp(string,pattern,d_ascii)