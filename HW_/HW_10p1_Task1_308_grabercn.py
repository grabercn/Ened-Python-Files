# Assignment Title: 10.1 Python 1 Sequential Task 1
# File: HW_10p1_Task1_308_grabercn.py 
# Date:    04 11 2021
# By:      Christian Graber
# Section: 022
# Team:    308
# 
# ELECTRONIC SIGNATURE
# Christian Graber
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# Takes the input of the amplitude of the incident wave, the permittivity, and
# and the permeability of 2 mediums. It then calculates intrinsic imperdances 
# of the 2 mediums and the amplitudes of the reflected and transmitted waves.


permittivityOne = float(input("Please enter the relative permittivity of material 1:"))
permeabilityOne = float(input("Please enter the relative permeability of material 1:"))
permittivityTwo = float(input('Please enter the relative permittivity of material 2:'))
permeabilityTwo = float(input("Please enter the relative permeability of material 2:"))
aiw = float(input("Please enter the amplitude of the incident wave (V/m):"))

n1 = 377.14*((permeabilityOne/permittivityOne)**(1/2))
n2 = 377.14*((permeabilityTwo/permittivityTwo)**(1/2))


print('Intrinsic Impedance 1:'+str(n1))
print('Intrinsic Impedance 2:'+str(n2))

transmittedAmplitude = ((2*n2)/(n2+n1))*aiw
reflectedAmplitude = ((n2-n1)/(n2+n1))*aiw

print("Reflected Amplitude: {0:.2f}".format(reflectedAmplitude))
print("Transmitted Amplitude: {0:.2f}".format(transmittedAmplitude))