# HW 12 Task 2 
# File: HW_12p1_Task2_grabercn.py
# Date:    18 11 2021
# By:      Christian Graber
# Section: 022
# Team:    308
# 
# ELECTRONIC SIGNATURE
# Christian Graber
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program is a simulation of the game sevens, where 2 players roll 2 dice until the sum of the 2 dice equals seven, and add up all the sums to get a score.
# The program then switches to the next player and has the player do the same thing. The first person to achieve or exceed the entered win score wins.

import random

winningScore = int(input('Enter the Winning Score: '))
Pn1 = str(input('Player Name 1: '))
Pn2 = str(input('Player Name 2: '))


diceP1 = random.randint(1,6)
diceP2 = random.randint(1,6)

order=0
pScore1=0
pScore2=0

while order==0:
    if (diceP1 > diceP2):
        order = 1
        print(Pn1+" goes first!")
    elif (diceP1 == diceP2):
        order = 0
    else: 
        order = 2
        print('')
        print(Pn2+" goes first!")


while (pScore1<winningScore or pScore2<winningScore):
    
    sum = 0
    input("Hit Enter When Ready ")
    
    while(sum!=7):
        
        roll = random.randint(1,6)
        roll2 = random.randint(1,6)
        sum = roll+roll2
        
        if roll==roll2:
            sum = sum*2
        
        
        if (order==1):
            print(Pn1+" rolled a "+str(roll)+" and a "+str(roll2))
            pScore1+=sum
        else:
            print(Pn2+" rolled a "+str(roll)+' and a '+str(roll2))
            pScore2+=sum
    
    print('--Current Scores--')
    print(Pn1+": "+str(pScore1))
    print(Pn2+": "+str(pScore2))
    
    if order==1:
        order=2
    else: order=2
    if pScore1>=winningScore:
        print(Pn1+" wins the game!")
        break
    elif pScore2>=winningScore:
        print(Pn2+" wins the game!")
        break