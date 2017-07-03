#include "FastLED.h"

#define NUM_LEDS 50
#define DATA_PIN 3
#define CLOCK_PIN 13

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() { 
       FastLED.addLeds<WS2812, DATA_PIN, RGB>(leds, NUM_LEDS);
}
    
unsigned long createRGBA(int r, int g, int b, int a)
{   
    return ((r & 0xff) << 24) + ((g & 0xff) << 16) + ((b & 0xff) << 8)
           + (a & 0xff);
}

bool up = true;
int i = 0;

void loop() { 
  
  if (up){
    i++;
  }else{
    i--;  
  }
  
  if ((i==255)||(i==0)){
     up = !up; 
  }
  
  LEDS.setBrightness(100);
//  leds[89] =createRGBA(255,0,0,i);

for(int j = 0 ; j<NUM_LEDS; j++){
  leds[j] =createRGBA(255,0,0,i);
}

  
//  leds[1] = CRGB::Blue;
//  leds[0] = CRGB::Green;
//  leds[9] =createRGBA(255,0,0,i);
//  leds[6] = CRGB::Blue;
//  leds[5] = CRGB::Green;
//    leds[14] =createRGBA(255,0,0,i);
//  leds[11] = CRGB::Blue;
//  leds[10] = CRGB::Green;
  FastLED.show();
}
