#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:30:14 2018

@author: jayneel
"""
from hangman import hangman
from beforegame import getword
#take word randomly from database


#Database Schema: Word Noofgames Noofsolved Noofmoveswhensolved difficulty

"""TRAINGING"""
def training():
    word,ngames,nsolved,nmoves,nhits,diff,z=getword()
    ntrials,corr,solved,score=hangman(word,z)
    print(solved)
    print(score)
    #resolving parameters
    nhits+=corr
    #difficulty update
    diff=(diff*ngames+corr/ntrials)/(ngames+1)
    print(diff)
    ngames+=1
    
    if solved==1:
        nsolved+=1
        nmoves+=ntrials
    else:
        nmoves+=10


    
    stri=word+":"+str(ngames)+":"+str(nsolved)+":"+str(nmoves)+":"+str(diff)+":\n"


    s = open("words1.txt").read()
    s = s.replace(z,stri)
    f = open("words1.txt", 'w')
    f.write(s)
    f.close()

    
#get word
#play hangman with the word
#nooftrials,correct hits,solved

#write appropriate result to database

#define levels based on difficulty.


#define words in each level.


"""Testing"""

#get id of user
def getlastid():
    file=open("user.txt","r")
    lastid=0
    for x in file:
        y=x.split(":")
        if y[0].isalnum()==True:
            lastid=int(float(y[0]))
    return lastid
    return""
def register():
    username=input("please enter your name")
    file=open("user.txt","a")
    userid=getlastid()
    stri="\n"+str(userid+1)+":"+str(0)+":"+str(0)+":"+str(0)+":"+username+":"
    file.write(stri)
    file.close()
    print("remember your id:"+str(userid+1))
    return userid+1
def main():
    print("do you have an id (yes/no)?")
    y=input().lower()
    if y=="yes":
        userid=int(float(input("Please enter your user id.")))
        play(userid)
    else:
        print("would you like to register(yes/no)?")
        y=input().lower()
        if y=="yes":
            userid=register()
            play(userid)
        else:
            print("i am sorry, you need to register. Please restart the app.")
        
def play(userid):
    
    file=open("user.txt","r")
    userlevel=0
    strrep=""
    userscore=0
    for x in file:
        user=x.split(":")
        #print(user)
        if int(float(user[0]))==userid:
            strrep=x
            ngamees=int(float(user[1]))
            userlevel=int(float(user[2]))
            userscore=int(float(user[3]))
            username=user[4]
#trialno,corr,solved,score
    print("Hi! "+username+", let us start the game!")
    word,ngames,nsolved,nmoves,nhits,diff,z=getword()
    ntrials,corr,solved,score=hangman(word,z)
    nhits+=corr
    #difficulty update
    diff=(diff*ngames+corr/ntrials)/(ngames+1)
    ngames+=1
    
    if solved==1:
        nsolved+=1
        nmoves+=ntrials
    else:
        nmoves+=10

    userscore=(diff*ngames+userscore)/(userscore+1)
    if userscore<0.25:
        userlevel=0
    elif userscore<0.5:
        userlevel=1
    elif userscore<0.75:
        userlevel=2
    elif userscore<1:
        userlevel=3
    else:
        userlevel=4
        
    nhits+=corr
    #difficulty update
    diff=(diff*ngames+corr/ntrials)/(ngames+1)
    print(diff)
    ngames+=1
    
    if solved==1:
        nsolved+=1
        nmoves+=ntrials
    else:
        nmoves+=10


    
    stri=word+":"+str(ngames)+":"+str(nsolved)+":"+str(nmoves)+":"+str(diff)+":\n"


    s = open("words1.txt").read()
    s = s.replace(z,stri)
    f = open("words1.txt", 'w')
    f.write(s)
    f.close()
    
    stri=str(userid)+":"+str(ngamees)+":"+str(userlevel)+":"+str(userscore)+":"+username+":"
    s = open("user.txt").read()
    s = s.replace(strrep,stri)
    f = open("user.txt", 'w')
    f.write(s)
    f.close()
#fetch user level, name using ID
#based on the level, fetch a level.

#randomly select a word from the database based on level.

#play hang man

#get results, and log the game details, and user level appropriately.
#write appropriate result to database

"""USAGE"""
main()
