""" Use this file to tune the controller.
    PID values, feed-forward and minPWM. 

"""

import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

# Set pid values.
p = 540
i = 200
d = 10

# Set log file name to be used.
log_fname = 'log_{}_{}_{}.txt'.format(p, i, d)

# Assign left and right motors.
motors = [1,2]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255

motorParams.pidParameters.k_p = p
motorParams.pidParameters.k_i = i
motorParams.pidParameters.k_d = d

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

interface.startLogging(log_fname)

while True:
	angle = float(input("Enter a angle to rotate (in radians): "))

	interface.increaseMotorAngleReferences(motors,[angle,angle])

	while not interface.motorAngleReferencesReached(motors) :
		motorAngles = interface.getMotorAngles(motors)
		if motorAngles :
			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
		time.sleep(0.1)

	print "Destination reached!"
	
interface.stopLogging(log_fname)
interface.terminate()
