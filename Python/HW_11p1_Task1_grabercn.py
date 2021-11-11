# Python Conditionals Task 1
# File: HW_11p1_Task1_grabercn
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
# This program takes the inputs Temperature, weather conditions, Relative humidity
# Number of ladders, Height of the structure, and Surface Dryness. It uses these values to compute
# Heat Related and Fall Related scores and outputs a needed action based on these scores.

T = float(input('Enter outside Temp in F (-10-125): '))
Wc = int(input('Enter Weather Conditions (3: sunny, 2: partly cloudy 0: cloudy): '))
H = float(input('Enter Relative Humidity (0-1): '))
L = float(input('Enter Number of Ladders on Construction Site: '))
Hstruc = float(input('Enter Height of Structure in ft (20-2800): '))
Sdry = int(input('Enter Surface Dryness (3: all surface wet, 2: puddles w some dry area, 0: completely dry): '))

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
if (Hstruc < 20 or Hstruc>2800):
    print('Height of Structure outside Range')
    t+=1
if (Sdry < 0 or Sdry > 3 or Sdry == 1):
    print('Surface Dryness outside Range')
    t+=1

if(t==0):  
    HRI = (0.75*T)+(5.0*Wc)+(H**2)

    if (HRI >75):
        Hcat = 1
    else:
        Hcat = 0
        
    FRI = (0.2*L)+(0.03*Hstruc)+(30*Hcat)+(10*Sdry)

    print('Heat Related Injury: {0:.1f}'.format(HRI))
    print('Fall Related Injury: {0:.1f}'.format(FRI))

    if(HRI>75):
        print('Site Manager Needs to Allow for 1 Extra Break')
    if(FRI>100):
        print('Site Manager Needs to Hold a Quick Safety Meeting')
    if not(FRI>100) or not(HRI>75):
        print("Safety is Job #1")