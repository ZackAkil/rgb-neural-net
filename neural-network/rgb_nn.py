
import urllib.request
import json
import numpy as np
import pandas as pd
import colorsys
from pprint import pprint

class RGB_NN():
# class for displaying NN weights on RGB NN of shape (2:3:2)

    _server_loc = 'http://192.168.1.162:5000'
    _url = _server_loc +'/change_leds'
    
    _blank_led_json = {"red":0, "green":0, "blue":0, "led_num":0}
    _led_num = 44
    _blank_leds_json = {}
    
    _brightness = 1
    
    def __init__(self, server_loc):
        self._server_loc = server_loc
        self._blank_leds_json = {"leds":[{**self._blank_led_json, "led_num":i} for i in range(self._led_num)]}
        
    def display_weights(self, clf):
        led_json = {"leds": self._make_led_coef_vals(clf)}
        return self._send_json(led_json)
    
    
    def _send_json(self, led_json):
        return led_json
        params = json.dumps(led_json).encode('utf8')
        req = urllib.request.Request(_url, data=params,
                                  headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(req)
        
    def _turn_off(self):
        _send_json(_blank_leds_json)
    
    def _val_to_rgb(self, val):
    # return [RED, GREEN, BLUE] for decimal 0.0 -> 1.0
        i = val*0.67
        c = colorsys.hsv_to_rgb(i,1,1)
        return [int((color*255)*self._brightness) for color in c]
    
    def _led_json_with_rgb_value(self, led_num, val):
        r, g, b = self._val_to_rgb(val)
        return {"led_num":led_num, "red":r, "green":g, "blue":b}
    
    
    # led mappings

    _input_layer_bias = [
        [8,9],
        [3,4]
    ]

    _input_layer_weights = [
        [[5,11],[6,20],[7,28]],
        [[0,10],[1,18],[2,27]]
    ]

    _hidden_layer_bias = [
        [13,14],
        [21,22],
        [29,30]
    ]

    _hidden_layer_weights = [
        [[16,41],[15,36]],
        [[23,40],[25,35]],
        [[31,39],[32,34]]
    ]

    _output_layer_bias = [
        [42,43],
        [37,38]
    ]
    
    def _map_weights_to_leds(self, coefs, led_map):
        leds = []
        for i,v in enumerate(led_map):
            for i2,v2 in enumerate(v):
                for led in v2:
                    led_json = self._led_json_with_rgb_value(led, coefs[i][i2])
                    leds.append(led_json)
        return leds

    def _map_biases_to_leds(self,bias, led_map):
        leds = []
        for i,v in enumerate(led_map):
            for led in v:
                led_json = self._led_json_with_rgb_value(led, bias[i])
                leds.append(led_json)
        return leds

    def _make_led_coef_vals(self, clf):
        leds = []
        leds += self._map_weights_to_leds(clf.coefs_[0], self._input_layer_weights)
        leds += self._map_weights_to_leds(clf.coefs_[1], self._hidden_layer_weights)
        leds += self._map_biases_to_leds(clf.intercepts_[0], self._hidden_layer_bias)
        leds += self._map_biases_to_leds(clf.intercepts_[1], self._output_layer_bias)
        return leds