import time
from gpiozero import DistanceSensor

print("Prepare GPIO pins")
left_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
right_sensor = DistanceSensor(echo=16, trigger=26, queue_len=2)

while True:
    print("Left: {l} Right: {r}".format(l = left_sensor.distance * 100, r = right_sensor.distance * 100)) # 
    time.sleep(0.2)