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
import Basic_Functions

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize here.
ev3 = EV3Brick()
motorLeft = Motor(Port.A)
motorRight = Motor(Port.D)

# Given Values go Here
laps = 4 # Laps (n)
DistInputMM = 900 # Defined Forward Distance (mm)

# Define dynamic values here.
speed = 500 # Motor Speed (deg/s)
time = 5000 # Motor Spin Time (ms)
DistInputMM = DistInputMM * -1 # Convernt defined dist to neg, since motors are on backwards

# Define Constants Here
Diameter = 2.204724 # Wheel Diameter (in)
DiameterMM = 2.5*25.4 # Wheel Diameter (mm)
axleTrack = 165.1 # Distance between the wheels where they touch the ground (mm)
moveErrorpMM = (31.75/1000) # Move error per mm (mm)
moveErrorMM = moveErrorpMM*(DistInputMM*-1) # estimated move error amount per lap (mm)



# Perform calculations Here
#lengths = laps*2 # Lengths (2n)
#rotations = (speed*(time/1000))/360 # Full motor rotations per lap
#DistTrav = (((Diameter * math.pi) * rotations)/12) # Calc Dist Travelled (ft)
DistTravLap = -1*(DistInputMM * (laps*2)) # Calc total Dist Travelled for all laps (mm)
moveErrorTotal = laps*moveErrorMM # total move error for all laps
moveErrorForward = (DistInputMM*-1)-((moveErrorMM/2)*(laps/2)) # Total dist with error forwards direction (mm)
moveErrorBackward = (DistInputMM*-1)+((moveErrorMM/2)*(laps/2)) # Total dist with error backwards (mm)

# Define and Call Robotics class to use built in functionss
driveFunc = DriveBase(motorLeft, motorRight, DiameterMM , axleTrack)
        
        
# Main Function starts here
def main():
    
    ev3.screen.clear() # Clear EV3 Screen
    
    # Print Values to Python Command Line 
    print('Current Voltage: '+str(ev3.battery.voltage()/1000))
    #print('Estimated Rotations: '+str(rotations))
    print('Estimated Dist Total (mm): '+str(DistTravLap))
    print('Distance Error (+/-) (mm): '+str(moveErrorTotal))
    print('Total Dist Est Forward (mm): '+str(moveErrorForward))
    print('Total Dist Est Backward (mm): '+str(moveErrorBackward))


    
    # Print Values to EV3 Screen
    #ev3.screen.print('ER:',rotations, sep=' ', end='\n')
    ev3.screen.print('DT Total:',DistTravLap, sep=' ', end='\n')
    ev3.screen.print('D Error(+/-):',moveErrorTotal, sep=' ', end='\n')

    
    
    # Statement for 2 cases: Even amount of laps (ex 2), and half amount of laps (ex 1.5) 
    if type(laps) == float:
        for i in range(1,round(laps)):
            print('-> Execute Odd')
            driveFunc.straight(DistInputMM)
            driveFunc.straight(-DistInputMM)
        driveFunc.straight(DistInputMM)
    else:
        for i in range(laps):
            print('-> Execute Even')
            driveFunc.straight(DistInputMM)
            driveFunc.straight(-DistInputMM)


main() # run main function