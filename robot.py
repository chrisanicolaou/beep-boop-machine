from motor_controller import MotorController
from distance_sensors import DistanceSensors
from led_controller import LedController

class Robot(object):
    def __init__(self) -> None:
        self.motor_controller = MotorController()
        self.sensors = DistanceSensors()
        self.led_controller = LedController()

    def set_left_motor(self, speed: int):
        self.motor_controller.set_left(speed)

    def set_right_motor(self, speed: int):
        self.motor_controller.set_right(speed)