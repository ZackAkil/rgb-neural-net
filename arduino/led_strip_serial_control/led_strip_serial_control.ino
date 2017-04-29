#include "FastLED.h"

#define NUM_LEDS 30
#define DATA_PIN 3
#define CLOCK_PIN 13

// Define the array of leds
CRGB leds[NUM_LEDS];




String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  FastLED.addLeds<WS2812, DATA_PIN, RGB>(leds, NUM_LEDS);
}

    
long createRGB(byte r, byte g, byte b)
{   
  long RGB = ((long)r << 16L) | ((long)g << 8L) | (long)b;
  return RGB;
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    
    int r = inputString.substring(0,3).toInt();
    int g = inputString.substring(3,6).toInt();
    int b = inputString.substring(6,9).toInt();
    int n = inputString.substring(9,11).toInt();
    
    
    leds[n] = createRGB(r,g,b);
    FastLED.show();
       
       
    Serial.println(r);
    Serial.println(g);
    Serial.println(b);
    Serial.println(n);
     
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}


