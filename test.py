from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

mh = Raspi_MotorHAT(addr=0x6f)
lm = mh.getMotor(1)
rm = mh.getMotor(2)

def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

def set_speed(speed):
    lm.setSpeed(speed)
    rm.setSpeed(speed)

def run_at_speed_for_duration(speed, dir = 1, alt_dir = 1, duration = 1):
    set_speed(speed)
    lm.run(dir)
    rm.run(alt_dir)
    time.sleep(duration)
    

# lm.setSpeed(220)
# rm.setSpeed(220)

run_at_speed_for_duration(255, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.FORWARD, 40)
# run_at_speed_for_duration(190)
# run_at_speed_for_duration(200, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.BACKWARD)
# #run_at_speed_for_duration(210)
# run_at_speed_for_duration(220, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.BACKWARD, 2)
# run_at_speed_for_duration(255, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.FORWARD, 2)

# start_speed = 180
# for x in range(start_speed, 40, -10):
#     print(x)
#     run_at_speed_for_duration(x, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.FORWARD)