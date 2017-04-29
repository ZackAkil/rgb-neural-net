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

### Resources

http://www.meccanismocomplesso.org/en/controlling-arduino-raspberry-pi/

https://forum.arduino.cc/index.php?topic=405287.0

https://github.com/FastLED/FastLED
