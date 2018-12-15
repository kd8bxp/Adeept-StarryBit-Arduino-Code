/*
Copyright (c) 2018 LeRoy Miller

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

If you find this or any of my projects useful or enjoyable please support me.  
Anything I do get goes to buy more parts and make more/better projects.  
https://www.patreon.com/kd8bxp  
https://ko-fi.com/lfmiller  

https://github.com/kd8bxp
https://www.youtube.com/channel/UCP6Vh4hfyJF288MTaRAF36w  
https://kd8bxp.blogspot.com/  
*/

/*
 * Micro:Bit LED Matrix Pins
 * The 5x5 matrix is not wired like a 5x5 matrix -
 * it is wired like a 9x3 matrix, with the 2 col
 * missing a couple of rows.
 * below is the matrix, each led uses two pins, 
 * one for high and one for low, these leds can be
 * reversed biased to do some light sensing.
 * 
 */

/*
        COL0   COL1    COL2    COL3    COL4
ROW 0: (3,26) (23,27) (4, 26) (24,27) (10,26)
ROW 1: (23,28) (24,28) (25,28) (9,28) (7,28)
ROW 2: (4, 27) (6,26) (10,27) (6,28) (3,27)
ROW 3: (7,26) (9,26) (25,26) (24,26) (23,26)
ROW 4: (10,28) (9,27) (3, 28) (25,27) (4,28)
 */

//This will blink the 1st LED on the Matrix (0,0) 
#define blinkPin1 3
#define blinkPin2 26


 //Adafruit's Microbit Library makes using the LED Matrix Easy
 
void setup() {

  pinMode(blinkPin1, OUTPUT);
  pinMode(blinkPin2, OUTPUT);

}

void loop() {
  digitalWrite(blinkPin1, LOW); //Make this pin LoW

 digitalWrite(blinkPin2, HIGH); 
 delay(1000);
 digitalWrite(blinkPin2, LOW);
 delay(1000);
}
