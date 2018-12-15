// Example for using Adafruit Bluefruit App to send/receive controller data

// BLE Serial code Copyright (c) Sandeep Mistry. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
//Softdevice S110 - Adafruit sketch adapted for use with the DF Robot Maqueen
//by LeRoy Miller (c) 2018

#include <Adafruit_Microbit.h>
Adafruit_Microbit microbit;

#define left1 14
#define left2 16 //pwm
#define right1 13
#define right2 15 //pwm

// function prototypes over in packetparser.cpp
uint8_t readPacket(Stream *ble, uint16_t timeout);
float parsefloat(uint8_t *buffer);
void printHex(const uint8_t * data, const uint32_t numBytes);
// the packet buffer
extern uint8_t packetbuffer[];

#define BLE_READPACKET_TIMEOUT 1000

void setup() {
  Serial.begin(9600);
  Serial.println("Controller demo ready!");
pinMode(left1, OUTPUT);
  pinMode(left2, OUTPUT);
  pinMode(right1, OUTPUT);
  pinMode(right2, OUTPUT);
  
stop(); //make sure motors are stopped

  // custom services and characteristics can be added as well
  microbit.BTLESerial.begin();
  microbit.BTLESerial.setLocalName("StarryBit");
microbit.begin();
}

/**************************************************************************/
/*!
    @brief  Constantly poll for new command or response data
*/
/**************************************************************************/
void loop(void)
{
  /* Wait for new data to arrive */
  uint8_t len = readPacket(&(microbit.BTLESerial), BLE_READPACKET_TIMEOUT);
  if (len == 0) return;

  /* Got a packet! */
  // printHex(packetbuffer, len);

  

  // Buttons
  if (packetbuffer[1] == 'B') {
    uint8_t buttnum = packetbuffer[2] - '0';
    boolean pressed = packetbuffer[3] - '0';
    Serial.print ("Button "); Serial.print(buttnum);
    if (pressed) {
      Serial.println(" pressed");
    } else {
      Serial.println(" released");
    }

 //Arduino PWM is from 0 to 255
  //ccw (counter clockwise) will move the car forward
  //in the python examples this is positive numbers.
  //cw (clockwise) will move the car backward
  //in the python examples this is the negitive numbers.
  //PWM for left, right motor 
//number keys 1 to 4 aren't used in this example.
switch (buttnum) {
  case 5:
  if (pressed) { ccw(100,100); } else { stop(); }
  break;
  case 6: 
  if (pressed) {cw(100,100); } else {stop(); }
  break;
  case 7: 
  if (pressed) {ccw(0,100); } else {stop();}
  break;
  case 8:
  if (pressed) {ccw(100,0); } else {stop();}
  break;
  default:
  stop();
  break;
  }
 }
}

void cw(int lft, int rgt) { 
  //This causes the car to move backward
  digitalWrite(left1, 1);
  digitalWrite(right1, 1);
  analogWrite(left2, map(lft,50,255,50,255));
  analogWrite(right2, map(rgt,50,255,50,255));  
}

void ccw(int lft, int rgt) {
  //This causes the car to move forward
  digitalWrite(left1, 0);
  digitalWrite(right1, 0);
  analogWrite(left2, lft);
  analogWrite(right2, rgt);
}

void stop() {
  digitalWrite(left1, 0);
  digitalWrite(right1, 0);
  analogWrite(left2, 0);
  analogWrite(right2, 0);
}


