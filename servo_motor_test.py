import Raspi_MotorHAT.Raspi_PWM_Servo_Driver
import atexit

# The PWM device is the same I2C device we are using for the wheel motors, and so has the same address
pwm = Raspi_MotorHAT.Raspi_PWM_Servo_Driver.PWM(0x6f)

# This sets the timebase for it all
pwm_frequency = 100
pwm.setPWMFreq(pwm_frequency)

# Lets call the middle pos 0 degrees. For most servos, turning to -90 degrees requires a pulse of 1 ms; going to the center requires 1.5ms.
servo_midpoint_ms = 1.5

# Turning it to 90 degrees requires a pulse of 2ms; 0.5ms from the midpoint, which gives us a primary calibration point for 90 degrees
deflect_90_in_ms = 0.5

# Frequency is 1 / period, but working ms, we can use 1000
period_in_ms = 1000 / pwm_frequency
# The chip has 4096 steps each period
pulse_steps = 4096
# Thus, steps every millisecond
steps_per_ms = pulse_steps / period_in_ms

# Steps for a degree 
steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90
# Midpoint of the servo in steps
servo_midpoint_steps = servo_midpoint_ms * steps_per_ms

def convert_degrees_to_steps(pos):
    return int(servo_midpoint_steps + (pos * steps_per_degree))

atexit.register(pwm.setPWM, 0, 0, 4096)

while True:
    pos = int(input("Type your position in degrees (90 to -90, 0 is middle): "))
    bus = int(input("Select your servo bus (0 is tilt, 1 is pan): "))
    end_step = convert_degrees_to_steps(pos)
    pwm.setPWM(bus, 0, end_step)