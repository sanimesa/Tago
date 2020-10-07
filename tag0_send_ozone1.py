# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:51:45 2020

@author: Shuvro Aikath
"""


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

my_device = tago.Device('2d474459-de11-4677-8012-f30c0ef2515b')

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
            'variable': 'ozone',                
            'unit'    : 'PPM',                                    
            'value'   : 55,                                                   
            'time'    : '2020-04-22 13:00:00',                           
}

cnt = 0

while True:
    data['value'] = round(random.uniform(0.001, 0.009),4)
    data['time'] = str(datetime.datetime.now())

    print(data)
    result = my_device.insert(data)
    print(result)
    cnt+=1
    print(cnt)
    time.sleep(15)
