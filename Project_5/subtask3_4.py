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
barcode = 3
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
turn_rate = 70 # Turn Rate (deg/s)
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
    moveArm(64,1000,True)
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
            driveStraight(5,"d")
        elif (box == 8):
            driveStraight(9,"r")
            turnAngle(90)
            driveStraight(3,"d")
        elif (box == 9):
            driveStraight(17.5,"r")
            turnAngle(90)
            driveStraight(-2,"u")
            moveArm(-120,1000,True)
            driveStraight(5,"d")  
        elif (box == 10):
            driveStraight(21,"r")
            turnAngle(90)
            driveStraight(3,"d") 
        elif (box == 11):
            driveStraight(27,"r")
            turnAngle(90)
            driveStraight(3,"d")  
        elif (box == 12):
            driveStraight(33,"r")
            turnAngle(90)
            driveStraight(3,"d") 
    elif(Above == False):
        if (box == 1):
            driveStraight(11,"u")
            turnAngle(-90)
            driveStraight(5,"r")
        elif (box == 2):
            driveStraight(9,"u")
            turnAngle(-90)
            driveStraight(3,"r")
        elif (box == 3):
            driveStraight(15,"u")
            turnAngle(-90)
            driveStraight(3,"r")  
        elif (box == 4):
            driveStraight(21,"u")
            turnAngle(-90)
            driveStraight(3,"r") 
        elif (box == 5):
            driveStraight(27,"u")
            turnAngle(-90)
            driveStraight(3,"r")  
        elif (box == 6):
            driveStraight(33,"u")
            turnAngle(-90)
            driveStraight(3,"r") 

# Move arm all the way down
# Input: None
def moveArmDown():
    motorArm.run_time(500, 1000, Stop.HOLD, True)


# ---------------Main Function-----------------------------#
def main():
    # Write your program here.
    
    #goBox(9) # go to box 9
    
    BarcodeRead = 3
    done = 0
    
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
    else:
        ev3.screen.clear()
        print("Barcode Read is "+str(BarcodeRead)+" which is not Barcode Given")
        ev3.screen.print("Barcode Read is "+str(BarcodeRead))
        ev3.screen.print("Not Barcode Given")
        wait(10000)
        
        ev3.speaker.beep()
        ev3.speaker.beep()
        
        # Run Barcode Read again if value was incorrect first time, reset arm first
        moveArm(-335,1000,True) # reset arm
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
        else:
            ev3.screen.clear()
            print("Barcode Read is "+str(BarcodeRead)+" which is not Barcode Given")
            ev3.screen.print("Barcode Read is "+str(BarcodeRead))
            ev3.screen.print("Not Barcode Given")
            
            nStep = False
            ev3.speaker.beep()
            ev3.speaker.beep()
            
            wait(10000)
    """
    
    turnAngle(-50) # Turn to face aisle
    
    # Drive to end of aisle
    totx = 55-x
    driveStraight(totx)
    
    moveArmDown() # Drop box
    
    ev3.speaker.beep() # Signifies End of Program
    
main()