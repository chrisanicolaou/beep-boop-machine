import os
import time
import logging
from gpiozero import DigitalInputDevice

class EncoderCounter(object):
    def __on_pin_changed(self, _, state):
        if self.state == state:
            self.logger.info(f"COUNT SKIPPED DUE TO DUPLICATE STATE! Pin number: {self.pin_num}. Count before increment: {self.pulse_count}. _: {_}. State: {state}")
            return
        self.logger.info(f"COUNT DETECTED. Pin number: {self.pin_num}. Count before increment: {self.pulse_count}. _: {_}. State: {state}")
        self.state = state
        self.pulse_count += 1

    def __init__(self, pin_num):
        self.state = 2
        self.pulse_count = 0
        self.last_event_time = -1
        self.pin_num = pin_num
        self.__encoder = DigitalInputDevice(pin_num)
        self.__encoder.pin.when_changed = self.__on_pin_changed
        file_name = os.path.basename(__file__)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(file_name)
        self.logger.setLevel(logging.INFO)

