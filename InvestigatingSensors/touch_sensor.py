"""

"""

import brickpi
# from ../AccurateRobotMotion/calibration import forward, backward, left90deg, right90deg

# init_interface()
interface = brickpi.Interface()
interface.initialize()

motors = [1, 2]
speed = 6.0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
motorParams.pidParameters.k_p = 100.0
motorParams.pidParameters.k_i = 0.0
motorParams.pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0], motorParams)
interface.setMotorAngleControllerParameters(motors[1], motorParams)


# init_touch_sensors()
touch_port = [0,1]

interface.sensorEnable(touch_port[0], brickpi.SensorType.SENSOR_TOUCH)
interface.sensorEnable(touch_port[1], brickpi.SensorType.SENSOR_TOUCH)

def run():
    while True:
        # move_forward()
        interface.setMotorRotationSpeedReferences(motors, [speed, speed])

        # get_touch_sensor_reading(left, right)
        l = interface.getSensorValue(touch_port[0])
        r = interface.getSensorValue(touch_port[1])

        # if both l and r, step back and rotate either left or right(left in this case).
        if l and r:
            backward()
            left90deg()

        if l:
            backward()
            right90deg()

        if r:
            backward()
            left90deg()

