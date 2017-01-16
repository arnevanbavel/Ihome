#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

import urllib2
import urllib

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN)

GPIO.setup(6,GPIO.OUT)  #Groen
GPIO.setup(12,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

GPIO.setup(27,GPIO.OUT) #Wit
GPIO.setup(9,GPIO.OUT)

GPIO.setup(19,GPIO.OUT) #Geel
GPIO.setup(16,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(26,GPIO.OUT) #Rood
GPIO.setup(20,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

GPIO.output(6,GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(23,GPIO.LOW)



print GPIO.input(22)
x = 0

def postdata(state):
    parameter = {'light':state}
    postData = urllib.urlencode(parameter)
    request = urllib2.Request("http://samdewachter.multimediatechnology.be/rasp/public/post", postData)
    con = urllib2.urlopen(request)

while True:
    if (GPIO.input(22) == False):
        x = x + 1
        print(x)
        time.sleep(0.5)
    if (x == 0):
        GPIO.output(6,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)
        postdata(0)
    elif (x == 1):
        GPIO.output(6,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(9,GPIO.HIGH)
        postdata(1)
    elif (x == 2):
        GPIO.output(27,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        postdata(2)
    elif (x == 3):
        GPIO.output(6,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        postdata(3)
    elif (x == 4):
        GPIO.output(6,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(9,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        GPIO.output(20,GPIO.HIGH)
        postdata(4)
    else:
        x = 0

