import math

while True:
    V0 = int(input('Enter Initial Velocity (m/s): '))
    theta = int(input('Enter Desired Angle Increment (deg): '))
    
    if not(0>theta>90):
        break
    if not(V0<=0):
        break
        

