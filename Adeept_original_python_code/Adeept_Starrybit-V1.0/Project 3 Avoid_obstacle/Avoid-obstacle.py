#-----------------------------------------------------------
# File name   : Avoid-obstacle.py
# Description : Avoid obstacles in front of you while driving.
# Author      : jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2018/10/10
#-----------------------------------------------------------
from microbit import *
import neopixel


# Initialise neopixels and define neopixels quantity
npix = neopixel.NeoPixel(pin8, 41)

# Define basic colours
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


def way():
    # define IR sensor
    IR = pin0.read_analog()
    if IR > 250:
    # Turn on
        LightAll(green)
        Drive(500, 500)
    else:
        LightAll(red)
        Drive(-300, 50)
        sleep(500)
    print(IR)


while True:
    way()