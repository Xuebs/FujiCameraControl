import time

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

import datetime
import os


FT232H.use_FT232H()

ft232h = FT232H.FT232H()

ft232h.setup(9, GPIO.IN)
ft232h.setup(8, GPIO.OUT)

while True:
    level = ft232h.input(9)
    if level == GPIO.HIGH:
        print 'level high'
    else:
        print 'level low'

