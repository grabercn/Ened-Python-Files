# Project 4: Codes
# File: Proj4_Team_GoStraightTurn.py 
# Date:    9 March 2022
# By:      Christian Graber and Team 040
# Section: 003
# Team:    040
# 
# ELECTRONIC SIGNATURE
# Christian Graber, Lauren Ulsh, Kyle Mares, Alyssa Kendall
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program makes the robot move forward, turn, then move forward again a specified number of inches.


#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Custom imports
import math

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize here
ev3 = EV3Brick()
motorLeft = Motor(Port.A)
motorRight = Motor(Port.D)

# Given Values go Here
DistInputIN = 9.25 # Defined Forward Dist (in)
DistInputIN2 = 96 + (6.5) # Defined Forward Dist After Turn (in) + Turning Dist (in)
turnAngle = -158 # Robot turn angle (deg*2)
# ------------------------------------------------------------------------------------
# Convert Dist Values
DistInputMM = DistInputIN*25.4 # Defined Forward Distance (mm)
DistInputMM2 = DistInputIN2*25.4 # Defined Forward Dist After Turn (mm)

# Define dynamic values here.
speed = 500 # Motor Speed (deg/s)
time = 5000 # Motor Spin Time (ms)
DistInputMM = DistInputMM * -1 # Convernt defined dist to neg, since motors are on backwards
DistInputMM2 = DistInputMM2 * -1

# Define Constants Here
Diameter = 2.204724 # Wheel Diameter (in)
DiameterMM = Diameter*25.4 # Wheel Diameter (mm)
axleTrack = 189 # Distance between the wheels where they touch the ground (mm)
turn_rate = 50 # Turn Rate (deg/s)
turn_acceleration = 50 # Turn Accel (deg/s/s)
straight_speed = 200 # Straight Speed (deg/s)
straight_acceleration = 500 # Straight Accel (deg/s/s)

# Perform calculations Here
# .....

# Define and Call Robotics class to use built in functionss
driveFunc = DriveBase(motorLeft, motorRight, DiameterMM , axleTrack)
        
# Main Function starts here
def main():
    
    ev3.screen.clear() # Clear EV3 Screen
    driveFunc.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    
    # Print Values to Python Command Line 
    print('Current Voltage: '+str(ev3.battery.voltage()/1000))

    # Print Values to EV3 Screen
    # ......

    # Move Forward, turn, and move forward again a diff amount
    print('-> Forward')
    ev3.speaker.beep()
    driveFunc.straight(DistInputMM)
    print('-> Turn')
    driveFunc.turn(turnAngle)
    print('-> Forward')
    driveFunc.straight(DistInputMM2)
    
main() # run main function