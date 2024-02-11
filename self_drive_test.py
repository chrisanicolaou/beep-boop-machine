import time
from gpiozero import DistanceSensor
from motor_controller import MotorController, Direction
import colorsys

import ledshim

spacing = 360.0 / 16.0
hue = 0

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.8)


def convert_distance_to_speed(dist):
    if (dist > 80):
        return 100
    if (dist < 25):
        return -100
    return dist
        

left_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
right_sensor = DistanceSensor(echo=16, trigger=26, queue_len=2)
motor_controller = MotorController()
time_limit = 10

while time_limit > 0:
    hue = int(time.time() * 100) % 360
    for x in range(ledshim.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        ledshim.set_pixel(x, r, g, b)

    ledshim.show()
    left_sensor_dist = (left_sensor.distance * 100) or 0
    right_sensor_dist = (right_sensor.distance * 100) or 0
    print("Left: {l} Right: {r}".format(l = left_sensor_dist, r = right_sensor_dist)) # 
    left_motor_speed = convert_distance_to_speed(left_sensor_dist)
    right_motor_speed = convert_distance_to_speed(right_sensor_dist)
    motor_controller.set_left(right_motor_speed)
    motor_controller.set_right(left_motor_speed)
    time.sleep(0.01)
    time_limit -= 0.01
    