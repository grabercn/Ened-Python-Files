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
    
    