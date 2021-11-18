# HW 12.1 Task 1
# File: HW_12p1_Task1_grabercn.py
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
# This program takes inputs for The initial velocity and Desired angle increment, and calulates the projectile's max height
# as well as calculated time it would take for the projectile to hit the ground. This is repeated until the value of theta is not higher than 90.

import math

y=0
g=9.81

while y<2:
    V0 = int(input('Enter Initial Velocity (m/s): '))
    theta = int(input('Enter Desired Angle Increment (deg): '))
    
    if not(theta>90 or theta<0):
        y+=1
    if not(V0 < 0):
        y+=1

i = 1
while theta<90:
    theta=22*i
    Mh = ((V0**2)*(math.sin(math.radians(theta))**2)/(2*g))
    It = ((2*V0)*math.sin(math.radians(theta))/(g))
    
    print('For Angle = {0:.2f} deg., Impact Time = {1:.2f} s and Max Height = {2:.2f} m'.format(theta, It, Mh))
    i+=1
    theta=22*i
    
    