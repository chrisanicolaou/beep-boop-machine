import atexit
from encoder_counter import EncoderCounter
from motor_controller import MotorController
from distance_sensors import DistanceSensors
from led_controller import LedController
from servos import Servos

class Robot(object):
    def __init__(self, motorhat_addr=0x6f):
        self.motor_controller = MotorController(motorhat_addr)
        self.sensors = DistanceSensors()
        self.led_controller = LedController()
        self.servos = Servos(motorhat_addr)
        self.left_encoder = EncoderCounter(5)
        self.right_encoder = EncoderCounter(6)
        atexit.register(self.__stop_all)

    def set_left_motor(self, speed: int):
        self.motor_controller.set_left(speed)

    def set_right_motor(self, speed: int):
        self.motor_controller.set_right(speed)
    
    def set_pan(self, angle):
        self.servos.set_servo_angle(1, angle)

    def set_tilt(self, angle):
        self.servos.set_servo_angle(0, angle)
    
    def __stop_all(self):
        self.motor_controller.stop_motors()
        self.servos.stop_all()