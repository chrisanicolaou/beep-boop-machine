import time
import math
from robot import Robot
from color import Color

bot = Robot()

def convert_distance_to_speed(dist):
    if (dist > 80):
        return 100
    if (dist < 25):
        return -100
    return dist

def get_range_of_leds_to_light(dist, is_right_sensor):
    distance_range = (80, 25)
    possible_leds_to_set = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    if (is_right_sensor):
        possible_leds_to_set = [x + 19 for x in possible_leds_to_set]
    
    clamped_dist = min(max(dist, distance_range[1]), distance_range[0])
    t = 1 - (clamped_dist - distance_range[1]) / (distance_range[0] - distance_range[1])
    num_of_leds_to_set = math.floor(t * (len(possible_leds_to_set)))
    print(clamped_dist)
    print(t)
    print(possible_leds_to_set)
    if (num_of_leds_to_set < 1):
        print(f"No leds to set for sensor! Is right: {is_right_sensor}")
        return []
    led_index_midpoint = math.floor(len(possible_leds_to_set) / 2)
    print(led_index_midpoint)
    leds_to_set = [possible_leds_to_set[led_index_midpoint]]
    if (num_of_leds_to_set < 2):
        print(f"Setting LED at position {leds_to_set[0]} for sensor! Is right: {is_right_sensor}")
        return leds_to_set
    for x in range(1, math.floor(num_of_leds_to_set / 2)):
        print(f"Appending leds at indexes {led_index_midpoint - x} and {led_index_midpoint + x}")
        leds_to_set.append(possible_leds_to_set[led_index_midpoint - x])
        leds_to_set.append(possible_leds_to_set[led_index_midpoint + x])
            
    print(f"Setting the following LEDS: {' '.join(map(str, leds_to_set))} for sensor! Is right: {is_right_sensor}")
    return leds_to_set


time_limit = 5

time.sleep(10)

while time_limit > 0:
    left_sensor_dist = (bot.sensors.left_sensor.distance * 100) or 0
    right_sensor_dist = (bot.sensors.right_sensor.distance * 100) or 0
    left_motor_speed = convert_distance_to_speed(left_sensor_dist)
    right_motor_speed = convert_distance_to_speed(right_sensor_dist)
    left_leds = get_range_of_leds_to_light(left_sensor_dist, False)
    right_leds = get_range_of_leds_to_light(right_sensor_dist, True)
    bot.led_controller.clear()
    if (len(left_leds) > 0): bot.led_controller.set_pixels(left_leds, Color.RED.value)
    if (len(right_leds) > 0): bot.led_controller.set_pixels(right_leds, Color.RED.value)
    bot.set_left_motor(right_motor_speed)
    bot.set_right_motor(left_motor_speed)
    time.sleep(0.01)
    time_limit -= 0.01
    