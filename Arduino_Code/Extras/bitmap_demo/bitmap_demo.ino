// This is a demo of the matrix driver code
// works with Adafruit GFX commands - its just
// a really small screen!
// https://learn.adafruit.com/adafruit-gfx-graphics-library

#include <Adafruit_Microbit.h>
#include "images.h"

Adafruit_Microbit_Matrix microbit;
    
void setup() {  
  Serial.begin(9600);
  
  Serial.println("microbit matrix demo is ready!");

  microbit.begin();
}
    
void loop(){
  // draw a heart
  microbit.show(microbit.HEART); //Included in Adafruit Library
  delay(3000);
  microbit.show(microbit.EMPTYHEART); //included in Adafruit library
  delay(3000);
  // draw a no cross
  microbit.show(microbit.NO); //Included in Adafruit Library
  delay(3000);

  // draw a yes check
  microbit.show(microbit.YES); //Included in Adafruit Library
  delay(3000);

//This are custom images from images.h 
//include images.h in your sketch if you wish to use these bitmaps

  microbit.show(smile_bmp); 
  delay(3000);
microbit.show(small_heart);
delay(3000);
microbit.show(sad);
delay(3000);
microbit.show(confused);
delay(3000);
microbit.show(up_arrow);
delay(3000);
microbit.show(down_arrow);
delay(3000);
microbit.show(left_arrow);
delay(3000);
microbit.show(right_arrow);
delay(3000);
microbit.show(ghost);
delay(3000);
microbit.show(skull);
delay(3000); 
  
}
