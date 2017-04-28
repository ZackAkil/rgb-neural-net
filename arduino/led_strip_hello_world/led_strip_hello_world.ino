#include "FastLED.h"

#define NUM_LEDS 30
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
  
  LEDS.setBrightness(32);
  leds[0] =createRGBA(255,0,0,i);
  leds[6] = CRGB::Blue;
  leds[20] = CRGB::Green;
  FastLED.show();
}
