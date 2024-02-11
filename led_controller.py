import ledshim

class LedController(object):
    def __init__(self) -> None:
        self.leds = ledshim
        self.leds.set_clear_on_exit()
    
    def set_pixel(self, index, rgb):
        self.leds.set_pixel(index, rgb[0], rgb[1], rgb[2])
        self.leds.show()
    
    def set_pixels(self, indexes, from_col, to_col = None):
        self.leds.set_multiple_pixels(indexes, from_col, to_col)
        self.leds.show()
    
    def clear(self):
        self.leds.clear()
        self.leds.show()