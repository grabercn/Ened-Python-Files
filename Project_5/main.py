#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

from MAIN_FUNCTIONS import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Given Values go Here
# Box number and section
shelf = "C1"
box = 5
ret = "C"
barcode = 2

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
turn_rate = 25 # Turn Rate (deg/s)
turn_acceleration = 50 # Turn Accel (deg/s/s)
straight_speed = 200 # Straight Speed (deg/s)
straight_acceleration = 500 # Straight Accel (deg/s/s)

#X and Y variables
global x
global y

# reset values
x = 0
y = 0

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

# Move arm a specified speed for a specified time, then wait or not
# Input: int Speed, int Time (ms), Bool Wait
def moveArm(speed, time, wait):
    
    # Reset the motor angle
    motorArm.reset_angle(0)
    
    #Invert Speed to match inverted motor
    speed=speed*-1
    
    #Run the motor for a specified amnt of time
    #if time is pos
    if (time > 0): 
        motorArm.run_time(speed, time, Stop.HOLD, wait)
    #if time is neg
    else: 
        motorArm.run_time(-1*speed, -1*time, Stop.HOLD, wait)

    
# Move arm all the way up
# Input: None
def moveArmUp():
    
    motorArm.run_time(-950, 1000, Stop.HOLD, True)
    
# Move arm all the way down
# Input: None
def moveArmDown():
    motorArm.run_time(500, 1000, Stop.HOLD, True)

# Drive to specific shelf, above or below determined by box
# Inputs: Shelf (string), Box (int)
def shelving(shelf, box):
    if(box> 6):
        above = True 
    else:
        above = False
    if((("A" in shelf or "B" in shelf) and "1" in shelf) and above == False):
        driveStraight(8,"u")
        turnAngle(90)
        if("B" in shelf):
            driveStraight(51,"r")
    elif((("A" in shelf or "B" in shelf) and "1" in shelf) and above == True):
        driveStraight(34.5,"u")
        turnAngle(89)
        if("B" in shelf):
            driveStraight(51,"r")
    elif((("A" in shelf or "B" in shelf) and "2" in shelf) and above == False):
        driveStraight(36,"u")
        turnAngle(90)
        if("B" in shelf):
            driveStraight(51,"r")
    elif((("A" in shelf or "B" in shelf) and "2" in shelf) and above == True):
        driveStraight(56,"u")
        turnAngle(90)
        if("B" in shelf):
            driveStraight(51,"r")
    elif((("C" in shelf or "D" in shelf) and "1" in shelf) and above == False):
        driveStraight(54,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(51,"r")
    elif((("C" in shelf or "D" in shelf) and "1" in shelf) and above == True):
        driveStraight(83,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(51,"r")
    elif((("C" in shelf or "D" in shelf) and "2" in shelf) and above == False):
        driveStraight(85,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(51,"r") 
    elif((("C" in shelf or "D" in shelf) and "2" in shelf) and above == True):
        driveStraight(107,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(51,"r")

# Go to a Specific Box, determined by box number
# Input: box (int)
def goBox(box):
    if (box>6):
        Above = True
    else:
        Above = False
    if (Above == True):
        if (box == 7):
            driveStraight(11,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")  
        elif (box == 8):
            driveStraight(14.25,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")  
        elif (box == 9):
            driveStraight(23,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")    
        elif (box == 10):
            driveStraight(25,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")   
        elif (box == 11):
            driveStraight(33,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")    
        elif (box == 12):
            driveStraight(40,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")   
    elif(Above == False):
        if (box == 1):
            driveStraight(11,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(7,"d")  
        elif (box == 2):
            driveStraight(14.25,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")  
        elif (box == 3):
            driveStraight(17.5,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")    
        elif (box == 4):
            driveStraight(25,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")   
        elif (box == 5):
            driveStraight(33,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")   
        elif (box == 6):
            driveStraight(40,"u")
            turnAngle(-90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")  

# Go to Box Dropoff location depending on current location
# Input: takes global variable ret (string)
def dropOff(ret):
    if (ret == "B"):
        if(box>6):
            turnAngle(-90)
            totx = 102 - x
            driveStraight(totx,"r")
            toty = y + 6
            turnAngle(90)
            driveStraight(toty,"d") 
        elif(box<=6):
            turnAngle(90)
            totx = 102 - x
            driveStraight(totx,"r")
            toty = y +6
            turnAngle(90)
            driveStraight(toty,"d")
    elif(ret == "D"):
        if(box>6):
            turnAngle(-90)
            totx = 102 - x
            driveStraight(totx,"r")
            toty = 114 - y
            turnAngle(-90)
            driveStraight(toty,"u") 
        elif(box<=6):
            turnAngle(90)
            totx = 102 - x
            driveStraight(totx,"r")
            toty = 114 - y
            turnAngle(-90)
            driveStraight(toty,"u") 
    elif(ret == "C"):
        if(box>6):
            driveStraight(-3,"d")
            turnAngle(90)
            totx = x
            driveStraight(totx,"l")
            toty = 114 - y
            turnAngle(90)
            driveStraight(toty,"u") 
        elif(box<=6):
            turnAngle(-90)
            totx = x
            driveStraight(totx,"l")
            toty = 114 - y
            turnAngle(90)
            driveStraight(toty,"u") 
            
# Goes back to Home A from any other Home
# Input: none
def goHome():
    if (ret == "C"):
        driveStraight(-10)
        turnAngle(180)
        driveStraight(110, "d")
        turnAngle(180)
    elif (ret == "B"):
        driveStraight(-6)
        turnAngle(90)
        driveStraight(102)
        turnAngle(-90)    
        driveStraight(6)
        turnAngle(180)
    elif(ret == "D"):
        driveStraight(-6)
        turnAngle(-90)
        driveStraight(102)
        turnAngle(-90)
        driveStraight(120)
        turnAngle(180)

# Read barcode and move up arm step by step, determine if matches from number given
# Input: int Barcode (barcode number looking for)
def readBarcode(barcode):
    # Color: False if Black, True if White
    color1 = False
    color2 = False
    color3 = False
    color4 = False
    
    # Recalibrate sensor for environment
    cal = (colorSensor.reflection()+30)
    
    if colorSensor.reflection() > cal:
        color1 = True
    moveArm(195,1000,True)
    wait(1000)
    if colorSensor.reflection() > cal:
        color2 = True
    moveArm(70,1000,True)
    wait(1000)
    if colorSensor.reflection() > cal:
        color3 = True
    moveArm(72,1000,True)
    wait(1000)
    if colorSensor.reflection() > cal:
        color4 = True
    
    print(color1,color2,color3,color4)
    color1 = False
    
    # Evaluate colors 1-4 to see if it matches parameter barcode number
    if color1 == False and color2 == True and color3 == True and color4 == True:
            return 1

    if color1 == False and color2 == True and color3 == False and color4 == True:
            return 2

    if color1 == False and color2 == False and color3 == True and color4 == True:
            return 3

    if color1 == False and color2 == True and color3 == True and color4 == False:
            return 4
    
    return 0




# ---------------Main Function-----------------------------#
def main():   
    # Write your program here.
    
    shelving(shelf, box) # go to shelf
    goBox(box) # go to box
    
    BarcodeRead = readBarcode(barcode) # read barcode 
    
    BarcodeRead = 0
    done = 0
    nStep = False
    
    while done < 4:
        
        BarcodeRead = readBarcode(barcode) # read barcode 
    
        #Determine if Barcode is Correct Read
        if BarcodeRead == barcode:
            ev3.screen.clear()
            print("Barcode Read is Barcode Given")
            ev3.screen.print("Barcode Read is")
            ev3.screen.print("Barcode Given")
            
            nStep = True
            ev3.speaker.beep()
            
            wait(10000)
            
            break
            
        else:
            ev3.screen.clear()
            print("Barcode Read is "+str(BarcodeRead)+" which is not Barcode Given")
            ev3.screen.print("Barcode Read is "+str(BarcodeRead))
            ev3.screen.print("Not Barcode Given")
            wait(10000)
        
            ev3.speaker.beep()
            wait(2000)
            ev3.speaker.beep()

            if BarcodeRead == 0:
                done = done + 1
                moveArm(-329,1000,True)
            else:
                break

    if nStep == True:
        driveStraight(-4,"u")
        dropOff(ret)
        moveArmDown()
        goHome()
    else:
        driveStraight(-4,"u")
        if box > 6:
            turnAngle(90)
        else:
            turnAngle(-90)
        
        driveStraight(x)
        turnAngle(-90)
        driveStraight(y)
        turnAngle(180)
    
    ev3.speaker.beep()
    
main()