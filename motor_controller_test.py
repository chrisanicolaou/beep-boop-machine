from motor_controller import MotorController
from time import sleep

motor_controller = MotorController()
motor_controller.steer_forward(100)
sleep(1)
motor_controller.reverse(100)
sleep(1)
motor_controller.steer_left(100, 30)
sleep(2)
motor_controller.reverse(80)
sleep(2)
motor_controller.steer_right(100, 10)
sleep(2)