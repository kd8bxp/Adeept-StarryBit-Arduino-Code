#-----------------------------------------------------------
# File name   : Motor.py
# Description : Back and forth.
# Author      : jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2018/10/10
#-----------------------------------------------------------
from microbit import *


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
    sleep(2000)
    Drive(-500, -500)
    sleep(2000)
    Drive(300, 1023)
    sleep(2000)
    Drive(-700, -1)
    sleep(2000)
    Drive(1023, 300)
    sleep(2000)
    Drive(-1, -700)
    sleep(2000)
    Drive(-1, 1023)
    sleep(3000)
    Drive(1023, -1)
    sleep(3000)
    Drive(0, 0)
    sleep(100000000)