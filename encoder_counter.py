import os
import time
import logging
from gpiozero import DigitalInputDevice

class EncoderCounter(object):
    def __on_pin_changed(self, _, state):
        self.pulse_count += 1

    def __init__(self, pin_num):
        self.pulse_count = 0
        self.__encoder = DigitalInputDevice(pin_num)
        self.__encoder.pin.when_changed = self.__on_pin_changed

