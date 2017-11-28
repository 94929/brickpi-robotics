import brickpi
import time

# init_interface()
interface = brickpi.Interface()
interface.initialize()

# init_sonar_sensor()
port = 2
interface.sensorEnable(port, brickpi.SensorType.SENSOR_ULTRASONIC);

while True:
    # ultrasonicReading = readValueFromPort()
    usReading = interface.getSensorValue(port)

    is usReading:
        print usReading
    else:
        print 'Failed usReading'

    time.sleep(0.05)

interface.terminate()

