from led_controller import LedController
from color import Color

l = LedController()

# Function to find enum member by name
def string_to_color(str):
    for member in Color:
        if member.name == str:
            return member.value
    return None


while True:
    pixels_input = input("Type the position of the LED(s) you wish to change (comma-separated): ")
    pixels = [int(x) for x in pixels_input.split(',')]
    col = string_to_color(input("Type your color ('red', 'green', 'blue', 'yellow' or 'purple'): ").upper())

    print (pixels)
    print (col)

    if (len(pixels) > 1):
        l.set_pixels(pixels, col)
    else:
        l.set_pixel(pixels, col)
