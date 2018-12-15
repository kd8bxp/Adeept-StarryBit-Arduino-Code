# Adeept Starry:Bit Robot Arduino IDE code ports

Code examples for the Arduino IDE using the Adeept Starry:Bit Robot
http://www.adeept.com/adeept-starrybit-bbc-microbit-smart-robot-car-kit-programmable-stem-educational-robot-kit-with-detailed-projects-tutorial-book_p0116_s0028.html  

Videos: https://www.youtube.com/playlist?list=PLvL2YQclXymc5q4Hw4X-9jBARlwPKl43_  

## Installation

Prerequisites: 
1) Install the Arduino-nRF5 board core. Follow instructions here:  
https://github.com/sandeepmistry/arduino-nRF5  
2) Install the Adafruit Micro:Bit Library.  
https://github.com/adafruit/Adafruit_Microbit and learn more about it here:  https://learn.adafruit.com/use-micro-bit-with-arduino   
3) Install the arduino-BLEPeripheral library by following instructions here:  
https://github.com/sandeepmistry/arduino-BLEPeripheral   
4) Install the NewPing Library: https://github.com/eliteio/Arduino_New_Ping  

Experimental, but useful:
Sparkfun's Mag3110 compass library - https://github.com/sparkfun/SparkFun_MAG3110_Breakout_Board_Arduino_Library   

Some help on installing the Arduino-nRF5 core on a linux machine.  
https://www.youtube.com/watch?v=ngZxVcUzUNo  

## Known Issues 
### or What is working and what is not working.

from time to time you have to reload the Micro:bit controller with a HEX file from
makecode, you may have to do this the first time you use it with the Arduino IDE.  
Generally I see this issue when I try to open the serial port before it's ready. Or if you switch a softdevice. Recommended to use softdevice 110, this is a must if you are using the Adafruit Library.  

The Starry:Bit robot has 40 Neopixels (WS2812) on PIN 8, currently this is not supported in any Neopixel library that I have seen. The Neopixels do work with the Makecode IDE, so this is a limitation of Arduino/Neopixel Libraries (I believe).  
There is a work around (thou I'm not sure I can recommend it).  
https://youtu.be/FIBGqRVVAX4  


The biggest issue I've run across so far is no peer-to-peer support in the Arduino IDE.  I am not even sure how it works. Again this is a non-issue with Makecode.  
BLE works, and Adafruit does provide an app for Android phones that support BLE. I was able to setup remote control via that app, and using one of Adafruits base sketches.  
https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect   
There is probably an app for IOS as well, but I don't own a IOS device.  

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Support Me

If you find this or any of my projects useful or enjoyable please support me.  
Anything I do get goes to buy more parts and make more/better projects.  
https://www.patreon.com/kd8bxp  
https://ko-fi.com/lfmiller  

## Other Projects

https://www.youtube.com/channel/UCP6Vh4hfyJF288MTaRAF36w  
https://kd8bxp.blogspot.com/  


## Credits

Copyright (c) 2018 LeRoy Miller

## License

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses>
