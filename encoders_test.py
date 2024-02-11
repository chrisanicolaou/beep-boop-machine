import os
import time
import logging
from encoder_counter import EncoderCounter
from motor_controller import MotorController

file_name = os.path.basename(__file__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(file_name)
logger.setLevel(logging.INFO)
left_encoder = EncoderCounter(5)
right_encoder = EncoderCounter(6)
motor_controller = MotorController()

motor_controller.set_left(80)
motor_controller.set_right(40)

stop_at_time = time.time() + 1.5

while time.time() < stop_at_time:
    logger.info(f"Left: {left_encoder.pulse_count} Right: {right_encoder.pulse_count}")
    time.sleep(0.05)

# while right_encoder.pulse_count < 40:
#     logger.info(f"Left: {left_encoder.pulse_count} Right: {right_encoder.pulse_count}")
#     time.sleep(0.05)