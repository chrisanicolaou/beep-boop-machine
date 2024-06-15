import math
import time

from robot import Robot

robot = Robot()

def get_circle_positions(radius, total_time, start_time):
    current_time = time.time() - start_time
    # Calculate the angle in radians
    angle = (current_time % total_time) / total_time * 2 * math.pi
    
    # Calculate X and Y positions
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    return x, y

# Example usage
radius = 30  # Radius of the circle
total_time = 8  # Time to complete one full circle (in seconds)
start_time = time.time()  # Record the start time

while True:
    x, y = get_circle_positions(radius, total_time, start_time)
    print(f"X: {x:.2f}, Y: {y:.2f}.")
    robot.set_pan(x)
    robot.set_tilt(y)
    time.sleep(0.03)  # Update the position every 0.1 seconds