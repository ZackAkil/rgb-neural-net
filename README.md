# RGB Neural Net
IOT physical neural network visualisation 

![net learning](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/nn%20wall%20learning.gif)

### What & Why?
This projects goal was to build an intuiative and visually interesting way of seeing a neural network learn. I built it becuase I had some empty wall space.

A separate computer runs the neural network training program and communicates with the RGB Neural Net over WiFi.


### Techincal components
Harware:
- 3D printed nodes
- Fibre optic tubing
- RGB LEDs
- Arduino Uno
- Raspberry Pi Zero

Software:
- RGB LED strip driver with serial com script on Arduino
- Flask API server running on Raspberry Pi taking requests and send intruction to Arduino via serial
- Python library that converts SciKit-Learn neural network model into the API requests for the Raspberry Pi


### What it does
The rgb network comprised of an array of rgb leds with side glow fiber optic tubing. An arduino drived teh led array, and a raspberry pi tell the arduino which leds to display. The raspberry pi acts as a local webserver and recieved API commands for what leds to turn on and which colour.


## Its making 
### Installing arduino to raspberr pi
```
sudo apt-get install arduino
```

### Turning on 20th LED
```python
import serial
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
arduinoSerialData.write('10010010020\n')
```

## Flask server API command

`POST /change_leds` sets the rgb values of multiple leds at once.

Json body:

```js
{
    "leds":
    [
        { "red": 0, "green": 200, "blue": 100, "led_num": 1 },
        { "red": 0, "green": 50, "blue": 100, "led_num": 2 },
        { "red": 0, "green": 50, "blue": 100, "led_num": 3 },
        { "red": 0, "green": 50, "blue": 100, "led_num": 4 }
    ]
}
```
 *^ this probably should have been a single dict with the key being the led number... ¯\\_(ツ)_/¯*

### To Do
- [x] Design neuron to 3D print
- [x] Print nodes
-   - [x] Input layer
-   - [x] Hidden layer
-   - [x] Output layer
- [x] Build electrics for nodes
-   - [x] 1 node
-   - [x] 2 node
-   - [x] 3 node
-   - [x] 4 node
-   - [x] 5 node
-   - [x] 6 node
-   - [x] 7 node
- [x] Embbed electronics nodes
-   - [x] 1 node
-   - [x] 2 node
-   - [x] 3 node
-   - [x] 4 node
-   - [x] 5 node
-   - [x] 6 node
-   - [x] 7 node
- [x] Test wire up
- [x] Optimise arduino code to update LEDs in batches
- [x] Optimise flask code to use new arduino code
- [x] Design mounting solution for nodes
- [x] Mount nodes on board
-   - [x] 1 node
-   - [x] 2 node
-   - [x] 3 node
-   - [x] 4 node
-   - [x] 5 node
-   - [x] 6 node
-   - [x] 7 node
- [x] Optically connect nodes
-   - [x] 1 node
-   - [x] 2 node
-   - [x] 3 node
-   - [x] 4 node
-   - [x] 5 node
-   - [x] 6 node
-   - [x] 7 node
- [x] Create LED mapper (to map to neuron weights)
-   - [x] Refactor server sending code into one doctument that:
-   -   [x] Sets an led to a value (one number converts to RGB)
#### Optional
- [ ] Get canvas
- [ ] Mount on canvas

### Resources

http://www.meccanismocomplesso.org/en/controlling-arduino-raspberry-pi/

https://forum.arduino.cc/index.php?topic=405287.0

https://github.com/FastLED/FastLED

### Notes

Serial communication was becoming incredably slow when testing sending alot of requests. This turns out to be becuase I had the arduino printing to the serial line whilst the raspberry pi was not reading it. This filled up the buffer of the arduino and puts a 1 second delay on all further communication.
https://arduino.stackexchange.com/questions/22816/serial-communication-dead-slow-after-a-while

When starting the server, the first led can become frozen at its initial colour, restarting the power to the strip will fix this.

Cooling: it seems that the little pi zero can get a bit flustered running as a server and thus either helping it with some cooling or upgrading to a beafier pi board is nessasary.

### Progress Images
Intital 3d design of nodes:
![3D neuron design](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/neuron-3d-design.png)
First and second interation of input/output node:
![printed input node](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/printed%20input%20node.jpg)
All nodes printed:
![network](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/printed%20network.jpg)
Soldered node lights:
![single node electrics](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/rgb%20neuron.jpg)
Electronics fitting in node shell:
![single node electrics](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/elec%20in%20node.jpg)
All electronics fitted in nodes 
![all nodes electrics](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/all%20wired.jpg)
All nodes connected and lighting up
![all nodes light up](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/net%20connected%20light.jpg)
Nodes mounted on boards
![all nodes electrics](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/nodes%20on%20board.jpg)
Nodes connected by fiber optic
![all nodes light up](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/optic%20connected%20nodes.jpg)
All nodes connected by fiber optic
![all nodes connected](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/full%20network.jpg)
High and low colour weights
![how node weights look](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/high%20low%20colour.jpg)

# Finaly!!!
RGB network connected up and displaying weights in real time from a learning sklearn NN multi-label cassifier model:
![final learning rgb nn](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/sklearn%20to%20rgb.jpg)

![net learning](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/net%20learning.gif)


