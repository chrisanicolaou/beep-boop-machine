from gpiozero import DistanceSensor

class DistanceSensors(object):
    def __init__(self) -> None:
        self.left_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
        self.right_sensor = DistanceSensor(echo=16, trigger=26, queue_len=2)
