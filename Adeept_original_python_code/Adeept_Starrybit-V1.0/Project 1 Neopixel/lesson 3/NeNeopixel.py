#-----------------------------------------------------------
# File name   : NeNeopixel.py
# Description : NeNeopixel.
# Author      : jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2018/10/10
#-----------------------------------------------------------
from microbit import *
import math
import neopixel

# Initialise neopixels
npix = neopixel.NeoPixel(pin8, 41)


# define all led
def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()


def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return (v, v, v)
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i % 6
    if i == 0:
        return (v, t, p)
    if i == 1:
        return (q, v, p)
    if i == 2:
        return (p, v, t)
    if i == 3:
        return (p, q, v)
    if i == 4:
        return (t, p, v)
    if i == 5:
        return (v, p, q)


# define MakeColour
def MakeColour(h):
    hsv = hsv_to_rgb(h, 1, 0.5)
    r, g, b = hsv
    return (math.floor(r*255), math.floor(g*255), math.floor(b*255))


# define Rainbow 
def Rainbow(delay):
    for pix in range(0, len(npix)):
        npix[pix] = MakeColour(pix/(len(npix)-1))
        npix.show()
        sleep(delay)


# define RainbowCycle
def RainbowCycle(delay):
    l = len(npix)
    colours = [MakeColour(i/(l-1)) for i in range(0, l)]
    for i in range(0, len(npix)):
        x = [colours[(i + j) % l] for j in range(0, l)]
        for pix in range(0, l):
            npix[pix] = x[pix]
        npix.show()
        sleep(delay)


while True:
    LightAll((128, 0, 0))
    sleep(1000)
    Rainbow(1000)
    sleep(1000)
    LightAll((128, 0, 0))
    sleep(1000)
    Rainbow(50)
    for i in range(0, 20):
        RainbowCycle(150)
    LightAll((128, 0, 0))
    sleep(1000)
    for i in range(0, 1000):
        RainbowCycle(20)
    sleep(1000)