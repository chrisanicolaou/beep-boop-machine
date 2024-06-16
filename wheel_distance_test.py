from math import pi
from time import sleep
from robot import Robot


bot = Robot()

start_delay = 10
distance_to_travel_in_mm = 1000
encoder_steps_per_wheel_turn = 40
wheel_diameter_in_mm = 66
distance_per_encoder_step = (pi * wheel_diameter_in_mm) / encoder_steps_per_wheel_turn

sleep(start_delay)
bot.motor_controller.set_left(70)
bot.motor_controller.set_right(100)
left_wheel_distance_travelled = 0
right_wheel_distance_travelled = 0

while left_wheel_distance_travelled < 1000:
    left_wheel_distance_travelled = distance_per_encoder_step * bot.left_encoder.pulse_count
    right_wheel_distance_travelled = distance_per_encoder_step * bot.right_encoder.pulse_count
    print(f"Left wheel distance travelled: {left_wheel_distance_travelled}mm. Right wheel distance travelled: {right_wheel_distance_travelled}mm")
    sleep(0.1)