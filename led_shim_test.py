import ledshim
import asyncio
import time
import colorsys

async def flash_led_async(pos, r, g, b):
    ledshim.set_pixel(pos, r, g, b)
    ledshim.show()
    await asyncio.sleep(2)
    ledshim.set_pixel(pos, 0, 0, 0)
    ledshim.show()

def flash_led(pos, r, g, b):
    ledshim.set_pixel(pos, r, g, b)
    ledshim.show()
    time.sleep(0.5)
    ledshim.set_pixel(pos, 0, 0, 0)
    ledshim.show()

async def flash_all_leds():
    for i in range(24):
        flash_led(i, i, i, 255-(i * (255 / 24)))

def main():
    flash_all_leds()

main()
time.sleep(10)
# ledshim.set_pixel(1, 255, 255, 255)
# ledshim.show()
# time.sleep(3)
