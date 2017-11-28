""" Distance and Rotation Calibration.

"""

import brickpi
import time

# Set angles for diffrent purposes.
movement_angle = 14.35
rotation_angle = 4.998

# Again, initialise motors to run.
motors = [1, 2]

def init_interface():
    interface = brickpi.Interface()
    interface.initialize()

    interface.motorEnable(motors[0])
    interface.motorEnable(motors[1])

    return interface

def init_motor_params(interface):
    motorParams = interface.MotorAngleControllerParameters()
    motorParams.maxRotationAcceleration = 6.0
    motorParams.maxRotationSpeed = 12.0
    motorParams.feedForwardGain = 255/20.0
    motorParams.minPWM = 18.0
    motorParams.pidParameters.minOutput = -255
    motorParams.pidParameters.maxOutput = 255
    motorParams.pidParameters.k_p = 380.0
    motorParams.pidParameters.k_i = 400.0
    motorParams.pidParameters.k_d = 40.0
    
    return motorParams

def set_interface(interface, motor_params):
    interface.setMotorAngleControllerParameters(motors[0],motor_params)
    interface.setMotorAngleControllerParameters(motors[1],motor_params)
    
def forward(interface):
    interface.increaseMotorAngleReferences(motors,[movement_angle, movement_angle])
    
    while not interface.motorAngleReferencesReached(motors):
        motorAngles = interface.getMotorAngles(motors)
        if motorAngles:
            print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)

def backward(interface):
    interface.increaseMotorAngleReferences(motors,[-movement_angle, -movement_angle])
    
    while not interface.motorAngleReferencesReached(motors):
        motorAngles = interface.getMotorAngles(motors)
        if motorAngles :
            print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)

def left90deg(interface):
    interface.increaseMotorAngleReferences(motors,[rotation_angle, -rotation_angle])

    while not interface.motorAngleReferencesReached(motors):
        motorAngles = interface.getMotorAngles(motors)
        if motorAngles :
            print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)

def right90deg(interface):
    interface.increaseMotorAngleReferences(motors,[-rotation_angle, rotation_angle])

    while not interface.motorAngleReferencesReached(motors):
        motorAngles = interface.getMotorAngles(motors)
        if motorAngles :
            print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)

def run(interface):
    forward(interface)
    right90deg(interface)
    forward(interface)
    left90deg(interface)
    backward(interface)
    left90deg(interface)
    forward(interface)

# Set variables to be used.
interface = init_interface()
motor_params = init_motor_params(interface)
set_interface(interface, motor_params)

# Run the Distance and Rotation Calibration.
run(interface)

interface.terminate()

