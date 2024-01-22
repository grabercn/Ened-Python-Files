
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

y = 0
x = 0

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
            driveStraight(50,"r")
    elif((("A" in shelf or "B" in shelf) and "1" in shelf) and above == True):
        driveStraight(34.5,"u")
        turnAngle(89)
        if("B" in shelf):
            driveStraight(50,"r")
    elif((("A" in shelf or "B" in shelf) and "2" in shelf) and above == False):
        driveStraight(30,"u")
        turnAngle(90)
        if("B" in shelf):
            driveStraight(50,"r")
    elif((("A" in shelf or "B" in shelf) and "2" in shelf) and above == True):
        driveStraight(54,"u")
        turnAngle(90)
        if("B" in shelf):
            driveStraight(50,"r")
    elif((("C" in shelf or "D" in shelf) and "1" in shelf) and above == False):
        driveStraight(54,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(50,"r")
    elif((("C" in shelf or "D" in shelf) and "1" in shelf) and above == True):
        driveStraight(78,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(50,"r")
    elif((("C" in shelf or "D" in shelf) and "2" in shelf) and above == False):
        driveStraight(78,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(50,"r") 
    elif((("C" in shelf or "D" in shelf) and "2" in shelf) and above == True):
        driveStraight(102,"u")
        turnAngle(90)
        if("D" in shelf):
            driveStraight(50,"r")

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
            driveStraight(15,"r")
            turnAngle(90)
            driveStraight(3,"d")  
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

# Go to Box Dropoff location depending on current location
# Input: takes global variable ret (string)
def dropOff(ret):
    if (ret == "B"):
        if(box>6):
            turnAngle(-90)
            totx = 102 - x
            driveStraight(totx,"r")
            toty = y +6
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