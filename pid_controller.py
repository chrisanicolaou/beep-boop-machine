import logging
logger = logging.getLogger("pid_controller")

class PIDController:
    def __init__(self, pK = 0, iK = 0):
        self.pK = pK
        self.iK = iK
        self.integral_sum = 0
    
    def handle_proportional(self, error):
        return self.pK * error
    
    def handle_integral(self, error):
        self.integral_sum += error
        return self.iK * self.integral_sum
    
    def get_value(self, error):
        p = self.handle_proportional(error)
        i = self.handle_integral(error)
        logger.debug(f"P: {p}, I: {i:.2f}")
        return p + i