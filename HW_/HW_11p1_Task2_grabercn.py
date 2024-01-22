
# Python Conditionals Task 2
# File: HW_11p1_Task2
# Date:    10 11 2021
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
# This program takes inputs for temperature, weather conditions, and relative
# humidity, and uses conditionals to determine and print an action accordingly.

T = float(input('Enter outside Temp in F (-10-125): '))
Wc = int(input('Enter Weather Conditions (3: sunny, 2: cloudy 0: raining): '))
H = float(input('Enter Relative Humidity (0-1): '))

t=0

if (T < -10 or T > 125):
    print("Outside Temp outside Range")
    t+=1
if (Wc <0 or Wc>3 or Wc==1):
    print('Weather Conditions outside Range')
    t+=1
if (H < 0 or H>1):
    print('Relative Humidity outside Range')
    t+=1

if (t==0):
    if(Wc == 0):
        print('Work Inside')
    elif(T>90):
        if(H>0.8 and Wc==3):
            print('Give two 15 Minute Breaks')
        elif(H>0.9 and Wc==2):
            print("Give one 15 Minute Break")
        else:
            print('Give one 10 Minute Break')
    elif(T>80 and T<90 and (H>0.9 and Wc==3)):
        print('Give two 10 Minute Breaks')
    elif(T>80 and T<90 and (H>0.9 or Wc==3)):
        print('Give one 10 Minute Break')
    else:
        print('No Extra Breaks')