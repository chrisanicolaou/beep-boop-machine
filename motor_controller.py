from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

from enum import Enum

import atexit

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class MotorController(object):
    def __init__(self, motorhat_addr=0x6f):
        self._mh = Raspi_MotorHAT(motorhat_addr)
        self.left_motor: Raspi_DCMotor = self._mh.getMotor(1)
        self.right_motor: Raspi_DCMotor = self._mh.getMotor(2)
        self.speed_tolerance = 0.01
        atexit.register(self.stop_motors)

    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)
    
    def steer_left(self, speed: int, severity: int = 25):
        self.steer(Direction.LEFT, speed, severity)
    
    def steer_right(self, speed: int, severity: int = 25):
        self.steer(Direction.RIGHT, speed, severity)
    
    def steer_forward(self, speed: int):
        self.__set_motor(speed, self.left_motor)
        self.__set_motor(speed, self.right_motor)
    
    def reverse(self, speed: int):
        self.__set_motor(-speed, self.left_motor)
        self.__set_motor(-speed, self.right_motor)

    def steer(self, dir: Direction, speed: int, severity: int = 25):
        faster_motor = self.right_motor if dir == Direction.LEFT else self.left_motor
        slower_motor = self.left_motor if dir == Direction.LEFT else self.right_motor
        self.__set_motor(speed, faster_motor)
        self.__set_motor(speed * (1 - severity / 100), slower_motor)
    
    def skid_steer(self, dir: Direction, speed: int):
        forward_motor = self.right_motor if dir == Direction.LEFT else self.left_motor
        backward_motor = self.left_motor if dir == Direction.LEFT else self.right_motor
        self.__set_motor(speed, forward_motor)
        self.__set_motor(-speed, backward_motor)
        

    def set_left(self, speed: int):
        self.__set_motor(speed, self.left_motor)

    def set_right(self, speed: int):
        self.__set_motor(speed, self.right_motor)
    
    def __set_motor(self, speed: int, motor: Raspi_DCMotor):
        mode, output_speed = self.__get_mode_and_converted_speed(speed)
        print("converted speed: " + str(output_speed))
        motor.setSpeed(output_speed)
        motor.run(mode)
    
    def __get_mode_and_converted_speed(self, speed: int):
        if abs(speed) < self.speed_tolerance:
            return mode, 0
        
        mode = Raspi_MotorHAT.FORWARD if speed > 0 else Raspi_MotorHAT.BACKWARD
        output_speed = ((abs(speed)) / 100 * 255)
        return mode, int(output_speed)