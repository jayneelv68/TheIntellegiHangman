#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:46:58 2018

@author: jayneel
"""

def hangman(word,diff):
    word=word.upper()
    solved=0
    score=diff
    #remove consonants
    word2=[]
    for x in word:
        word2.append(x)
        
    #print(word2)
    word1=word2
    for x in range(0,len(word1)):
        #print(x)
        if word1[x] not in ["A","E","I","O","U"]:
            #bvreak string into array
            word2[x]="_"
    #start guessing
    guesses=[]
    trialno=0
    corr=0
    maxtrial=10
    wrongno=0
    
    while wrongno<maxtrial and solved==0:
        if trialno>0:
            
            print("No of trials:"+str(trialno))
            print("Guesses left:"+str(maxtrial-wrongno))
            print("Misses:"+str(wrongno))
            print("Hits:"+str(corr))
            print("Guesses Made:")
            print(guesses)
            
        print(word1)
        
        guess=input("Make your guess").upper()
        hit=0
        if guess not in guesses and guess not in  ["A","E","I","O","U"] and len(guess)==1 and guess.isalpha():
            hit=0
            for x in range(0,len(word1)):
                if word[x]==guess:
                    word1[x]=guess
                    hit=1
                    #print("HIT UPDATED"+word1[x]+"==="+guess)
                
            trialno=trialno+1
            guesses.append(guess)
            
        else:
            if guess.isalpha()==False:
                print("Abeh, character dheela hai")
            elif len(guess)!=1:
                print("Enter a valid English Consonant")
            elif guess in ["A","E","I","O","U"]:
                print("Vowels kyu dal raha hai bey!")
            else:
                print("You have already tried that! why give off a  try!")
        if hit==1:
                corr=corr+1
                #print("Hit")
        else:
                wrongno=wrongno+1
            #print(str(wrongno))
        
        if "_" not in word1:
                    solved=1
        if hit==1:
            print("Hit")
            
        else:
            
            print("Nope,not there")
            
        
    if solved==1:
        print("Yeaaay, solved! You cracked the word:"+word) 
    else:
        print("Try again, the word was:"+word)
    if solved==0 and trialno==maxtrial:
        print("Your trials are over.")
        print("Final word:")
        print(word1)
        print("Guesses made were")
        print(guesses)
    score=0
    return trialno,corr,solved,score
