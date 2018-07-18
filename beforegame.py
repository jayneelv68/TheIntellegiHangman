#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:33:05 2018

@author: jayneel
"""
import random
def getword():
    file=open("words1.txt","r")
    nlines=0
    for x in file:
        nlines+=1
    choice=random.randint(1, nlines)
    #print(nlines)
    file.close()
    c=1
    found=""
    #print(c)
    #print(choice)
    file=open("words1.txt","r")
    for x in file:
        #print("c"+str(c)+"choice"+str(choice))
        if c==choice:
            found=x
            break
        c+=1
    wordarr=found.split(":")
    #print(wordarr)
    file.close()
    word=wordarr[0]
    ngames=float(int(wordarr[1]))
    nsolved=float(int(wordarr[2]))
    nmoves=float(int(wordarr[3]))
    nhits=float(int(wordarr[4]))
    diff=float(int(wordarr[5]))
    return word,ngames,nsolved,nmoves,nhits,diff,x
    