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
import numpy

my_device = tago.Device('11c190ab-7cb8-4b06-8daf-72d82f4f27fd')

"""
The following code defines the set of data to be sent to TagoIO
data fields:
- variable name
- variable unit
- variable value
- Optional: desired data timestamp 
- Optional: lat/long location (associated to your data) 
"""
data1 = {
            'variable': 'ozone',                
            'unit'    : 'PPM',                                    
            'value'   : 55,                                                   
            'time'    : '2020-04-22 13:00:00',                           
}

data = {
            'variable': 'ozone',                
            'unit'    : 'PPM',                                    
            'value'   : 55
}

cnt = 0

while cnt < 40:
    data['value'] = round(random.uniform(0.001, 0.009),4)
    #data['time'] = str(datetime.datetime.now())

    print(data)
    result = my_device.insert(data)
    print(result)
    cnt+=1
    print(cnt)
    time.sleep(15)
    
d_event = datetime.datetime.now()

#ozone cycle
for i in range(-16, 20, 2):
    data['value'] = round(numpy.exp(i/10), 4)
    #data['time'] = str(datetime.datetime.now())  #commented to get current UTC time defaulted as event time 
    result = my_device.insert(data)
    time.sleep(15)

#steady state    
for i in range(1, 100):
    data['value'] = round(random.uniform(4.9, 5.7), 4)
    #data['time'] = str(datetime.datetime.now())
    result = my_device.insert(data)
    time.sleep(15)
    

#ramp down cycle 
for i in range(18, -16, -1):  #the ramp down is more gradual than the ramp up 
    data['value'] = round(numpy.exp(i/10), 4)
    #data['time'] = str(datetime.datetime.now())
    result = my_device.insert(data)
    time.sleep(15)
    
while True:
    data['value'] = round(random.uniform(0.001, 0.009),4)
    #data['time'] = str(datetime.datetime.now())

    print(data)
    result = my_device.insert(data)
    print(result)
    cnt+=1
    print(cnt)
    time.sleep(15)    

