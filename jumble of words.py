# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:15:55 2020

@author: cprit
"""
import random
def choose():
    words=['hello','good','praise','admire']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def play():
    p1name=input("Enter the first player name-")
    p2name=input("Enter the second player name-")
    sc1=0
    sc2=0
    turn=0
    c=1
    while(c==1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if(turn%2==0):
            print(p1name,"it's your turn")
            ans=input("Guessthe write word-")
            if(ans==picked_word):
                print("You are right")
                sc1=sc1+1
                print("your score is",sc1)
            else:
                print("Answer is",picked_word)
                print("Your score is",sc1)
            c=int(input("Continue or not?"))
            if(c==0):
                print("Thank you",p1name)
                break
        else:
            print(p2name,"it's your turn")
            ans=input("Guessthe write word")
            if(ans==picked_word):
                print("You are right")
                sc2=sc2+1
                print("your score is",sc2)
            else:
                print("Answer is",picked_word)
                print("your score is",sc2)
            c=int(input("Continue or not?"))
            if(c==0):
                print("Thank you",p2name)
                break
        turn=turn+1
play()
            
                
            
            
            