import logging
import time

from pid_controller import PIDController
from robot import Robot


logger = logging.getLogger("straight_line_drive_test")
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pid_controller").setLevel(logging.DEBUG)

bot = Robot()
stop_at_time = time.time() + 15
speed = 80
bot.set_left_motor(80)
bot.set_right_motor(80)
pid = PIDController(pK=5, iK=0.3)

while time.time() < stop_at_time:
    time.sleep(0.01)
    left = bot.left_encoder.pulse_count
    right = bot.right_encoder.pulse_count
    error = left - right
    logger.info(f"Error: {error}. Left count: {left}. Right count: {right}")
    adjustment = pid.get_value(error)
    right_speed = int(speed + adjustment)
    left_speed = int(speed - adjustment)
    bot.set_left_motor(left_speed)
    bot.set_right_motor(right_speed)