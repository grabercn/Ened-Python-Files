# Assignment Title (include Task number if applicable)
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
# This program is a header template that will be used for 
# all your python files the rest of the semester.


permittivityOne = float(input("Please enter the relative permittivity of material 1:"))
permeabilityOne = float(input("Please enter the relative permeability of material 1:"))
permittivityTwo = float(input('Please enter the relative permittivity of material 2:'))
permeabilityTwo = float(input("Please enter the relative permeability of material 2:"))
amplitudeIncidentWave = float(input("Please enter the amplitude of the incident wave (V/m):"))

intrinsicImpedanceOne = 377.14*((permeabilityOne/permittivityOne)**(1/2))
intrinsicImpedanceTwo = 377.14*((permeabilityTwo/permittivityTwo)**(1/2))


print('Intrinsic Impedance 1:'+str(intrinsicImpedanceOne))
print('Intrinsic Impedance 2:'+str(intrinsicImpedanceTwo))

transmittedAmplitude = ((2*intrinsicImpedanceTwo)/(intrinsicImpedanceTwo+intrinsicImpedanceOne))*amplitudeIncidentWave
reflectedAmplitude = ((intrinsicImpedanceTwo-intrinsicImpedanceOne)/(intrinsicImpedanceTwo+intrinsicImpedanceOne))*amplitudeIncidentWave

print("Reflected Amplitude: {0:.2f}".format(reflectedAmplitude))
print("Transmitted Amplitude: {0:.2f}".format(transmittedAmplitude))