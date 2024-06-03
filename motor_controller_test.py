from motor_controller import MotorController, Direction
from time import sleep

sleep(10)
motor_controller = MotorController()
motor_controller.steer_forward(100)
sleep(1)
motor_controller.reverse(100)
sleep(1)
motor_controller.skid_steer(Direction.LEFT, 100)
sleep(1)
motor_controller.skid_steer(Direction.RIGHT, 100)
sleep(1)