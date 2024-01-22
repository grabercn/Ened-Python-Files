# Basic EV3 Functions for Tasks 1 and 2, using dynamic inputs

def moveForward(speed,time):
    speed = speed*-1
    motorLeft.run_time(speed,time,then=Stop.HOLD, wait=False)
    motorRight.run_time(speed,time,then=Stop.HOLD, wait=True)

def moveBackward(speed,time):
    speed = speed*1
    motorLeft.run_time(speed,time,then=Stop.HOLD, wait=False)
    motorRight.run_time(speed,time,then=Stop.HOLD, wait=True)

def rotate(speed,time):
    print('wow')