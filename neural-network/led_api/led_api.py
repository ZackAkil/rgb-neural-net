import json
import urllib.request

server_loc = 'http://192.168.1.162:5000'
url = server_loc +'/change_leds'

def send_led_json(led_json):
    params = json.dumps(led_json).encode('utf8')
    req = urllib.request.Request(url, data=params,
                              headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

# newConditions = {
#     "leds":[
#         { "red": 0, "green": 200, "blue": 100, "led_num": 1 },
#         { "red": 0, "green": 50, "blue": 100, "led_num": 2 },
#         { "red": 0, "green": 50, "blue": 100, "led_num": 3 },
#         { "red": 0, "green": 50, "blue": 100, "led_num": 4 },
#         { "red": 0, "green": 50, "blue": 100, "led_num": 5 },
#         { "red": 0, "green": 50, "blue": 100, "led_num": 6 }
#     ]
# }
# send_led_json(newConditions)