#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

import urllib2

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN)
GPIO.setup(6,GPIO.OUT)  #Groen
GPIO.setup(12,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT) #wit
GPIO.setup(27,GPIO.OUT)
GPIO.setup(19,GPIO.OUT) #geel
GPIO.setup(16,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26,GPIO.OUT) #rood
GPIO.setup(20,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(6,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.setup(23,GPIO.LOW)
time.sleep(30)

while True:
    time.sleep(5)
    try:
        con = urllib2.urlopen("http://samdewachter.multimediatechnology.be/rasp/public/get")

        if con.getcode() == 200:
            x = con.read()
            print x
    except urllib2.HTTPError, e:
        print e.getcode()
        
    if (x == "0"):
        GPIO.output(6,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
    elif (x == "1"):
        GPIO.output(6,GPIO.LOW)     #wit
        GPIO.output(12,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
    elif (x == "2"):
        GPIO.output(27,GPIO.LOW)    #Groen
        GPIO.output(18,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
    elif (x == "3"):
        GPIO.output(6,GPIO.LOW) #Geel
        GPIO.output(18,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
    elif (x == "4"):
        GPIO.output(6,GPIO.LOW) #Rood
        GPIO.output(12,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        GPIO.output(20,GPIO.HIGH)
    else:
        x = 0

