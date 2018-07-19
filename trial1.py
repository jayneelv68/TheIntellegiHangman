#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:30:14 2018

@author: jayneel
"""
from hangman import hangman
from beforegame import getword
#take word randomly from database
word,ngames,nsolved,nmoves,nhits,diff,z=getword()


#Database Schema: Word Noofgames Noofsolved Noofmoveswhensolved difficulty

"""TRAINGING"""

#get word

#play hangman with the word
#nooftrials,correct hits,solved
ntrials,corr,solved=hangman(word)
print(solved)
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

#write appropriate result to database

#define levels based on difficulty.


#define words in each level.


"""Testing"""

#get id of user
#fetch user level, name using ID
#based on the level, fetch a level.

#randomly select a word from the database based on level.

#play hang man

#get results, and log the game details, and user level appropriately.
#write appropriate result to database

