#-----------------------------------------------------------
# File name   : L1-Motor.py
# Description : Reciprocating.
# Author      : jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2018/10/10
#-----------------------------------------------------------
from microbit import *
import neopixel


# define pin8 control 41 Neopixel
npix = neopixel.NeoPixel(pin8, 41)

# define color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
nocol = (0, 0, 0)


# define all light
def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return


# define Drive
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


while True:
    Drive(500, 500)
    LightAll(green)
    sleep(4000)
    LightAll(red)
    Drive(-500, -500)
    sleep(4000)
    Drive(0, 0)
    npix.clear()
    sleep(100000000)