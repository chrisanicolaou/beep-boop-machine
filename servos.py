import atexit
from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM

class Servos(object):
    def __init__(self, addr=0x6f, deflect_90_in_ms=0.5):
        self.__pwm = PWM(0x6f)
        pwm_frequency = 100
        self.__pwm.setPWMFreq(pwm_frequency)
        servo_midpoint_ms = 1.5
        deflect_90_in_ms = 0.5
        period_in_ms = 1000 / pwm_frequency
        pulse_steps = 4096
        steps_per_ms = pulse_steps / period_in_ms
        self.steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90
        self.servo_midpoint_steps = servo_midpoint_ms * steps_per_ms
        self.__channels = [0, 1, 14, 15]
        atexit.register(self.stop_all)

    def stop_all(self):
        off_bit = 4096
        for channel in self.__channels:
            self.__pwm.setPWM(channel, 0, off_bit)
    
    def set_servo_angle(self, channel, angle):
        if angle > 90 or angle < -90:
            raise ValueError("Angle outside of range")
        off_step = self.__convert_degrees_to_steps(angle)
        self.__pwm.setPWM(self.__channels[channel], 0, off_step)
    
    def __convert_degrees_to_steps(self, pos):
        return int(self.servo_midpoint_steps + (pos * self.steps_per_degree))

