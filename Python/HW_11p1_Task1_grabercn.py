

T = int(input('Enter outside Temp in F (-10-125): '))
Wc = int(input('Enter Weather Conditions (3: sunny, 2: partly cloudy 0: cloudy): '))
H = int(input('Enter Relative Humidity (0-1): '))
L = int(input('Enter Number of Ladders on Construction Site: '))
Hstruc = int(input('Enter Height of Structure in ft (20-2800): '))
Sdry = int(input('Enter Surface Dryness (3: all surface wet, 2: puddles w some dry area, 0: completely dry): '))

if (T < -10 or T > 125):
    print("Outside Temp outside Range")
if (Wc <0 or Wc>3 or Wc==1):
    print('Weather Conditions outside Range')
if (H < 0 or H>1):
    print('Relative Humidity outside Range')
if (Hstruc < 20 or Hstruc>2800):
    print('Height of Structure outside Range')
if (Sdry < 0 or Sdry > 3 or Sdry == 1):
    print('Surface Dryness outside Range')
    

    
HRI = (0.75*T)+(5.0*Wc)+(H**2)

if (HRI >75):
    Hcat = 1
else:
    Hcat = 0
    
FRI = (0.2*L)+(0.03*Hstruc)+(30*Hcat)+(10*Sdry)

print('Heat Related Injury: {0:.1f}'.format(HRI))
print('Fall Related Injury: {0:.1f}'.format(FRI))

if(HRI>75):
    print('Site Manager Needs to Allow for 1 Extra Break')
if(FRI>100):
    print('Site Manager Needs to Hold a Quick Safety Meeting')
if not(FRI>100) or not(HRI>75):
    print("Safety is Job #1")