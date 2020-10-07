# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:39:22 2020

@author: Shuvro Aikath
"""


import tago
import json
import datetime
import random
import time

my_device = tago.Device('a7e93332-a26f-4689-a9cf-88b7db33fe11')

"""
The following code defines the set of data to be sent to TagoIO
data fields:
- variable name
- variable unit
- variable value
- Optional: desired data timestamp 
- Optional: lat/long location (associated to your data) 
"""
data = {
            'variable': 'temperature',                
            'unit'    : 'F',                                    
            'value'   : 55,                                                   
            'time'    : '2020-04-22 13:00:00',                           
            'location': {'lat': 42.2974279, 'lng': -85.628292}    
}

cnt = 0

while True:
    data['value'] = round(random.uniform(51, 60), 2)
    data['time'] = str(datetime.datetime.now())

    print(data)
    result = my_device.insert(data)
    print(result)
    cnt+=1
    print(cnt)
    time.sleep(30)
