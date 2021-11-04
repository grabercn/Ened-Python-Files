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
# This program is a header template that will be used for 
# all your python files the rest of the semester.

import math

intrinsicImpedanceOne = float(input('Please enter the intrinsic impedance of material 1:'))
phaseConstantOne = float(input("Please enter the phase constant of material 1:"))
intrinsicImpedanceTwo = float(input("Please enter the intrinsic impedance of material 2:"))
phaseConstantTwo = float(input("Please enter the phase constant of material 2:"))
amplitudeIncidentWave = float(input("Please enter the amplitude of the incident wave (V/m):"))

incidenceTheta = (math.asin(math.sqrt(((phaseConstantTwo**2)*((intrinsicImpedanceTwo**2)-(intrinsicImpedanceOne**2))/(((intrinsicImpedanceTwo**2)*(phaseConstantOne**2)-((intrinsicImpedanceOne**2)*(phaseConstantTwo**2))))))))
incidenceAngle = (incidenceTheta*(180/math.pi))

transmittedTheta = (math.acos((intrinsicImpedanceOne*math.cos((incidenceTheta)))/intrinsicImpedanceTwo)
transmittedAngle = ((transmittedTheta)*(180/math.pi))

reflectedAngle = incidenceAngle

reflectedAmplitude = (((intrinsicImpedanceTwo)*(math.cos(incidenceTheta)))-((intrinsicImpedanceOne*math.cos(transmittedTheta)))/((intrinsicImpedanceTwo)*(math.cos(incidenceTheta)))+((intrinsicImpedanceOne*math.cos(transmittedTheta)))*amplitudeIncidentWave)


print('Incident Angle: {0:2f}'.formatformat (incidenceAngle))
print('Reflected Angle: {0:2f}'.format (reflectedAngle))
print('Transmitted Angle: {0:2f}'.format (transmittedAngle))
print('Reflected Amplitude: {0:2f}'.format (reflectedAmplitude))