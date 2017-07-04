from flask import Flask, request
import serial

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/change_leds', methods=['POST'])
def change_leds():
    data = request.get_json()
    leds = data.get('leds')
    for led in leds:
        send_led_change_command(led['red'], led['green'], led['blue'], led['led_num'])
    commit_led_changes()
    return 'Done'

def send_led_change_command(red, green, blue, led_num):
    format_red = "%03d" % int(red)
    format_green = "%03d" % int(green)
    format_blue = "%03d" % int(blue)
    format_led_num = "%02d" % int(led_num)

    message_to_send = '{0}{1}{2}{3}\n'.format(format_green,
                                              format_red,
                                              format_blue,
                                              format_led_num)
    send_message_to_arduino(message_to_send)

def commit_led_changes():
    send_message_to_arduino('0')

def send_message_to_arduino(message_to_send):
    arduinoSerialData.write(bytes(message_to_send, 'UTF-8'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
