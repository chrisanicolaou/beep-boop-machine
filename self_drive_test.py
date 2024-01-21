from time import sleep
from gpiozero import DistanceSensor
from motor_controller import MotorController, Direction


def convert_distance_to_speed(dist):
    if (dist > 80):
        return 100
    if (dist < 25):
        return -100
    return dist
        

left_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
right_sensor = DistanceSensor(echo=16, trigger=26, queue_len=2)
motor_controller = MotorController()
time_limit = 5

while time_limit > 0:
    left_sensor_dist = (left_sensor.distance * 100) or 0
    right_sensor_dist = (right_sensor.distance * 100) or 0
    print("Left: {l} Right: {r}".format(l = left_sensor_dist, r = right_sensor_dist)) # 
    left_motor_speed = convert_distance_to_speed(left_sensor_dist)
    right_motor_speed = convert_distance_to_speed(right_sensor_dist)
    motor_controller.set_left(left_motor_speed)
    motor_controller.set_right(right_motor_speed)
    sleep(0.1)
    time_limit -= 0.1
    