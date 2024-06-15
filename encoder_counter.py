import os
import time
import logging
from gpiozero import DigitalInputDevice

from encoder_direction import EncoderDirection

class EncoderCounter(object):
    def __init__(self, pin_num, direction = 1):
        self.direction = direction
        self.__setup_logger()
        self.pulse_count = 0
        self.state = -1
        self.last_event_time = -1
        self.pin_num = pin_num
        self.__encoder = DigitalInputDevice(pin_num)
        self.__encoder.pin.when_changed = self.__on_pin_changed
    
    def __on_pin_changed(self, _, state):
        if self.state == state:
            self.logger.info(f"COUNT SKIPPED DUE TO DUPLICATE STATE! Pin number: {self.pin_num}. Count before increment: {self.pulse_count}. _: {_}. State: {state}")
            return
        self.logger.info(f"COUNT DETECTED. Pin number: {self.pin_num}. Count before increment: {self.pulse_count}. _: {_}. State: {state}")
        self.state = state
        self.pulse_count += self.direction

    def __setup_logger(self):
        file_name = os.path.basename(__file__)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(file_name)
        self.logger.setLevel(logging.INFO)
    
    def set_direction(self, direction: EncoderDirection):
        self.direction = direction.value
    
    def reset(self):
        self.pulse_count = 0
    
    def stop(self):
        self.__encoder.close()
    

