# RGB Neural Net

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
- [ ] Create led mapper (to map to neuron weights)
- [ ] Mount on board
- [ ] Get canvas
- [ ] Mount on canvas

### Resources

http://www.meccanismocomplesso.org/en/controlling-arduino-raspberry-pi/

https://forum.arduino.cc/index.php?topic=405287.0

https://github.com/FastLED/FastLED

### Notes

Serial communication was becoming incredably slow when testing sending alot of requests. This turns out to be becuase i had teh arduino printing stuff to the serial line aswell and the raspberry pi was not readining it. This filled up the cach of the arduino and puts a 1 second delay on all further communication.
https://arduino.stackexchange.com/questions/22816/serial-communication-dead-slow-after-a-while

When starting the server, the first led can become frozen at its initial colour, restarting the power to the strip will fix this.

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
