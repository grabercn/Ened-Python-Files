# Assignment Title (include Task number if applicable)
# File: HW_10p1_Task2_308_grabercn.py 
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
# This program takes inputs for the intrinsic impedance
# phase constant of two materials, as well as the amplitude of the incident wave.
# It then uses these to calculate the incident, reflected, and transmitted angles
# as well as the reflected and transmitted amplitudes.

import math

n1 = float(input('Please enter the intrinsic impedance of material 1:'))
b1 = float(input("Please enter the phase constant of material 1:"))
n2 = float(input("Please enter the intrinsic impedance of material 2:"))
b2 = float(input("Please enter the phase constant of material 2:"))
aiw = float(input("Please enter the amplitude of the incident wave (V/m):"))

incidenceT = (math.asin(math.sqrt((b2**2*((n2**2)-(n1**2)))/(((n2**2)*(b1**2))-((n1**2)*(b2**2))))))
incidenceA = (incidenceT*(180/math.pi))

transmittedT = (math.acos((n1*math.cos((incidenceT)))/n2))
transmittedA = ((transmittedT)*(180/math.pi))

reflectedAngle = incidenceA

reflectedAmplitude = ((((n2)*(math.cos(incidenceT))))-((n1)*(math.cos(transmittedT))))/(((n2)*(math.cos(incidenceT)))+((n1)*(math.cos(transmittedT))))*(aiw)
transmittedAmplitude = (((2)*(n2)*(math.cos(incidenceT)))/(((n2)*(math.cos(transmittedT)))+(n1)*(math.cos(incidenceT))))*(aiw)

print('Incident Angle: {0:.2f} degrees'.format (incidenceA))
print('Reflected Angle: {0:.2f} degrees'.format (reflectedAngle))
print('Transmitted Angle: {0:.2f} degrees'.format (transmittedA))
print('Reflected Amplitude: {0:.2f} V/m'.format (reflectedAmplitude))
print('Transmitted Amplitude: {0:.2f} V/m'.format (transmittedAmplitude))