# RGB Neural Net
IOT physical neural network visualization 

![net learning](images/nn%20wall%20learning.gif)

### What & Why?
This projects goal was to build an intuitive and visually interesting way of seeing a neural network learn. I built it because I had some empty wall space.

A separate computer runs the neural network training program and communicates with the RGB Neural Net over WiFi.

### Using the RGB Neural Net
First I generate some data that I want the neural network to learn. In this case it's some multi label classification data, meaning that given an 'x' and a 'y' value (2 continuous features) a data point can either have label A, label B, both label A and B, or no label assigned to it. i.e Label A could be 'if someone likes apples', and label B could be 'if someone like oranges', and therefore someone could like one, or the other, or both, or neither.
There generated data looks like the following:
![net learning](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/syth%20data.png)

Then in our program (python + sklearn) when create a neural network that is the same shape as the RGB one (1 hidden layer with 3 nodes).
```python
nn = MLPClassifier(hidden_layer_sizes=(3), 
                   activation='logistic', 
                   learning_rate_init=0.02, 
                   max_iter=1, warm_start=True)
```
Then import the RGB library and create the connection to the RGB neural network:
```python
from rgb_nn import RGB_NN
rgb = RGB_NN(server_loc='http://192.168.1.153:5000')
```
Finally just loop over the fitting of the code neural network along with the function to update the RGB neural network:
 ```python
 for i in range(50):
    nn.fit(X_train, y_train)
    rgb.display_weights(nn)
```
Then sit back and watch the learning happen:
![net learning](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/net%20learning.gif)

### What the colours mean
The colours of the connections represents the value of the weights between nodes (RED - Low, BLUE - 0, GREEN - High). The colours of the nodes themselves represent the bias value. 
![net key](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/nn%20key.png)


### Technical components
Hardware:
- 3D printed nodes
- Fibre optic tubing
- RGB LEDs
- Arduino Uno
- Raspberry Pi Zero

Software:
- RGB LED strip driver with serial com script on Arduino
- Flask API server running on Raspberry Pi taking requests and send instruction to Arduino via serial
- Python library that converts SciKit-Learn neural network model into the API requests for the Raspberry Pi



# Its making 
### Installing Arduino to Raspberry Pi
```
sudo apt-get install arduino
```

### Turning on 20th LED from Raspberry Pi
```python
import serial
# create serial connection
arduino_serial_connection = serial.Serial('/dev/ttyACM0',9600)
# send serial message
arduino_serial_connection.write('10010010020\n')
```

## Flask server API command

`POST /change_leds` sets the RGB values of multiple LEDs at once.

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
- [x] Embeded electronics nodes
-   - [x] 1 node
-   - [x] 2 node
-   - [x] 3 node
-   - [x] 4 node
-   - [x] 5 node
-   - [x] 6 node
-   - [x] 7 node
- [x] Test wire up
- [x] Optimise Arduino code to update LEDs in batches
- [x] Optimise flask code to use new Arduino code
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
-   - [x] Re-factor server sending code into one document that:
-   -   [x] Sets an led to a value (one number converts to RGB)
#### Optional
- [ ] Get canvas
- [ ] Mount on canvas

### Resources

http://www.meccanismocomplesso.org/en/controlling-arduino-raspberry-pi/

https://forum.arduino.cc/index.php?topic=405287.0

https://github.com/FastLED/FastLED

### Notes

Serial communication was becoming incredibly slow when testing sending a lot of requests. This turns out to be because I had the Arduino printing to the serial line whilst the Raspberry Pi was not reading it. This filled up the buffer of the Arduino and puts a 1 second delay on all further communication.
https://arduino.stackexchange.com/questions/22816/serial-communication-dead-slow-after-a-while

When starting the server, the first led can become frozen at its initial colour, restarting the power to the strip will fix this.

Cooling: it seems that the little pi zero can get a bit flustered running as a server and thus either helping it with some cooling or upgrading to a beefier pi board is necessary.

### Progress Images
Initial 3D design of nodes:
![3D neuron design](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/neuron-3d-design.png)
First and second interaction of input/output node:
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

# Finally!!!
RGB network connected up and displaying weights in real time from a learning sklearn NN multi-label classifier model:
![final learning rgb nn](https://raw.githubusercontent.com/ZackAkil/rgb-neural-net/master/images/sklearn%20to%20rgb.jpg)
