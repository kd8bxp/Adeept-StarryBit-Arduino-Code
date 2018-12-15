from microbit import *
import neopixel

# Initialise neopixels and define neopixels quantity
npix = neopixel.NeoPixel(pin8, 41)

# Define basic colours
red = (255, 0, 0)
green = (0, 255, 0)
redd = (220, 20, 60)

# define all light
def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return


# define left light
def LightLeft(col):
    for pix in range(26, 40):
        npix[pix] = col
    npix.show()
    return


# define right light
def LightRight(col):
    for pix in range(6, 20):
        npix[pix] = col
    npix.show()
    return


# define back light
def Lightback(col):
    for pix in range(20, 26):
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


# keep on following the line forever
while True:
    Finder = pin1.read_analog()
    if Finder > 1000:
        # Turn on
        Drive(500, 500)
        sleep(50)
        LightAll(green)
    elif Finder > 800 and Finder < 900:
        # Turn left
        Drive(-300, 1023)
        sleep(50)
        LightLeft(red)
        LightRight(green)
    elif Finder > 500 and Finder < 600:
        # Turn right
        Drive(1023, -300)
        sleep(50)
        LightRight(red)
        LightLeft(green)
    elif Finder > 200 and Finder < 300:
        # Turn on
        Drive(500, 500)
        sleep(50)
        LightAll(green)
    elif Finder > 100 and Finder < 199:
        # Turn on
        Drive(500, 500)
        sleep(50)
        LightAll(green)