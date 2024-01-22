#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

import MAIN_FUNCTIONS

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Given Values go Here
# Box number and section
shelf = "A1"
box = 1
ret = "B"

# ------------------------------------------------------------------------------------
# ------------------ Helper Values -----------------------#

# Define dynamic values here.
speed = 500 # Motor Speed (deg/s)
time = 5000 # Motor Spin Time (ms)
overshoot = 15

# Define Constants Here
Diameter = 2.204724 # Wheel Diameter (in)
DiameterMM = Diameter*25.4 # Wheel Diameter (mm)
axleTrack = 220 # Distance between the wheels where they touch the ground (mm)
turn_rate = 100 # Turn Rate (deg/s)
turn_acceleration = 100 # Turn Accel (deg/s/s)
straight_speed = 200 # Straight Speed (deg/s)
straight_acceleration = 500 # Straight Accel (deg/s/s)

#X and Y variables
global x
global y

y = 0
x = 0

# Initialize all objects here.
ev3 = EV3Brick()
motorLeft = Motor(Port.A, Direction.CLOCKWISE, [8,24,40,24,24,8])
motorRight = Motor(Port.D, Direction.CLOCKWISE, [8,24,40,24,24,8])
motorArm = Motor(Port.B)
colorSensor = ColorSensor(Port.S1)
ultraSonic = UltrasonicSensor(Port.S3)
gyroSensor =  GyroSensor(Port.S2,Direction.CLOCKWISE)

# Define and Call Robotics class to use built in functionss
driveFunc = DriveBase(motorLeft, motorRight, DiameterMM , axleTrack)
driveFunc.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)


# ----------------Helper Functions -----------------------#

# Convert inch to mm 
# Input: inches, output: mm
def inchtomm(inch):
    mm = inch * 25.4
    return mm

# Turn Angle to Degree, adjust using gyro for exact degree
# Input: Angle (deg)
def turnAngle(angle):
    
    gyroSensor.reset_angle(0)

    # reset angle rotation degree to 0
    #if angle > 0:
        #if ((gyroSensor.angle() - angle) != 0):
            #gyroSensor.reset_angle(0)
    #else:
        #if ((gyroSensor.angle() + angle) != 0):
            #gyroSensor.reset_angle(0)

    # Adjust angle innacuracy
    #if angle > 0 :
        #angle = angle - 1 #- round(angle*(0.025), 0)
    
    
    #driveFunc.turn(-1*(angle)) # Turn the robot negative angle amount
    
    if (angle > 0):
        # Turn clockwise until the angle is reached
        driveFunc.drive(0, -1*turn_rate)

        ev3.speaker.beep()

        while gyroSensor.angle() < angle - overshoot:
            wait(1)
        driveFunc.drive(0, 0)
        wait(1000)
    else:
    # Turn counter-clockwise until the angle is reached
        driveFunc.drive(0,turn_rate)

        ev3.speaker.beep()

        while gyroSensor.angle() > angle + overshoot:
            wait(1)
        driveFunc.drive(0, 0)
        wait(1000)
    
    # Determine if angle is pos or neg value
    #if (angle < 0):
        #While Angle is Neg Val
        #while (gyroSensor.angle() != angle):
            #If gyrosensor angle is not same as turn angle
            #Turn robot to equal input angle, left or right depending on over/under
            #if (gyroSensor.angle() > angle):
                
                
                
                #driveFunc.turn(angle)
            #elif (gyroSensor.angle() < angle):
                #driveFunc.turn(-1*angle)
    #else:
        #While Angle is Pos Val
        #while (gyroSensor.angle() != angle):
            #Turn robot to equal input angle, left or right depending on over/under
            #if (gyroSensor.angle() > angle):
                #driveFunc.turn(angle)
            #elif (gyroSensor.angle() < angle):
                #driveFunc.turn(-1*angle)

# Drive Straight a certain number of inches
# Input: inches, direction (u,d,l,r)
def driveStraight(inches, direction = "n"):
    global y 
    global x
    #Use x and y to estimate total position on x,y
    if direction == "u":
        y = y + inches
    elif direction == "d":
        y = y - inches
    elif direction == "l":
        x = x - inches
    elif direction == "r":
        x = x + inches
    else:
        direction = "n"
     
    inches = inches*-1 # invert inches bc of backwards motor
    
    #Move forward straight set inches
    driveFunc.straight(inchtomm(inches))
    return            

# ---------------Main Function-----------------------------#
def main():
    # Write your program here.
    
    #turnAngle(180) # turn back around
    driveStraight(6) # go forward
    turnAngle(-80) # turn left

    # Go to Home A
    totx = 102
    driveStraight(totx,"r")
    toty = -6
    turnAngle(90)
    driveStraight(toty,"d") 

    
    ev3.speaker.beep()
    
main()