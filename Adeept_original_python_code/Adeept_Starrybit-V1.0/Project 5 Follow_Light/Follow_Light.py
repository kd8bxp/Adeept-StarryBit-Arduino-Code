#-----------------------------------------------------------
# File name   : Follow_Light.py
# Description : Move to where the light is strong.
# Author      : jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2018/10/10
#-----------------------------------------------------------
from microbit import *
import neopixel

# Initialise neopixels
npix = neopixel.NeoPixel(pin8, 6)


# define colour
green = (0, 255, 0)


def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()


# define drive
def Drive(lft, rgt):
    pin14.write_digital(0)
    pin13.write_digital(0)
    if lft < 0:
        pin14.write_digital(1)
        lft = 1023 + lft
    if rgt < 0:
        pin13.write_digital(1)
        rgt = 1023 + rgt
    pin16.write_analog(lft)
    pin15.write_analog(rgt)


def Findlight():
    LightAll(green)
    Pho = pin2.read_analog()
    if Pho < 400:
        # left
        Drive(100, 800)
    elif Pho > 750:
        # right
        Drive(800, 100)
    else:
        # Go on
        Drive(400, 400)
    sleep(20)


while True:
    Findlight()
    sleep(20)