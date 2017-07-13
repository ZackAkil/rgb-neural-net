
def unwrap_to_pairs(l):
    o = []
    if type(l[0]) == list:
        for i in l:
            x = unwrap_to_pairs(i)
            if type(x[0]) != list:
                o += [x]
            else:
                o += x
        return o
    else:
        print(l)
        return l
    
def unwrap_to_singles(l):
    o = []
    if type(l[0]) == list:
        for i in l:
            o += unwrap_to_singles(x)
        return o
    else:
        print(l)
        return l

input_layer_bias = [
                    [8,9],
                    [3,4]
                    ]

input_layer_weights = [
                        [[5,11],[6,20],[7,28]],
                        [[0,10],[1,18],[2,27]]
                        
                      ]

hidden_layer_bias = [
                        [13,14],
                        [21,22],
                        [29,30]
                    ]

hidden_layer_weights = [
                            [[16,41],[15,36]],
                            [[23,40],[25,35]],
                            [[31,39],[32,34]]
                       ]

output_layer_bias = [
                        [42,43],
                        [37,38]
                    ]

weight_index =  (unwrap_to_pairs(input_layer_weights) + 
                 unwrap_to_pairs(hidden_layer_weights)
                )

bias_index =    (input_layer_bias +
                 hidden_layer_bias +
                 output_layer_bias)

def map_weight_to_led(coefs, led_map):
    leds = []
    for i,v in enumerate(led_map):
        for i2,v2 in enumerate(v):
            print(i,i2,v2,coefs[i][i2])
            for led in v2:
                leds.append({"led_num":led, "val":coefs[i][i2]})
    return leds

def map_bias_to_led(bias, led_map):
    leds = []
    for i,v in enumerate(led_map):
        print(i,v,bias[i])
        for led in v:
            leds.append({"led_num":led, "val":bias[i]})
    return leds

def make_led_coef_vals(clf):
    leds = []
    leds += map_weight_to_led(clf.coefs_[0], input_layer_weights)
    leds += map_weight_to_led(clf.coefs_[1], hidden_layer_weights)
    leds += map_bias_to_led(clf.intercepts_[0], hidden_layer_bias)
    leds += map_bias_to_led(clf.intercepts_[0], output_layer_bias)
    return leds