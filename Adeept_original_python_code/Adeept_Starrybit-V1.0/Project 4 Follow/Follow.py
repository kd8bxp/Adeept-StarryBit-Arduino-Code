#-----------------------------------------------------------
# File name   : Follow.py
# Description : Follow the object back and forth.
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
yellow = (255, 255, 0)
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


def Flow():
    # define IR sensor
    IR = pin0.read_analog()
    if IR > 150 and IR < 600:
        Drive(300, 300)
        LightAll(green)
    if IR < 150:
        Drive(-800, -800)
        LightAll(red)
    if IR > 600:
        Drive(0, 0)
        LightAll(yellow)


while True:
    Flow()
    sleep(20)