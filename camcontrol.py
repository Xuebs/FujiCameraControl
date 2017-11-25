import time

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

import datetime
import os


FT232H.use_FT232H()

ft232h = FT232H.FT232H()

ft232h.setup(9, GPIO.IN)
ft232h.setup(8, GPIO.OUT)

startIndex = eval(raw_input("Enter current index + 1: "))

with open('results.txt', 'w') as f:

    print 'Camera control ready'

    while True:
        
        if (ft232h.input(9) == GPIO.LOW):
            timeSignal = datetime.datetime.now()

            print'signal time: ', timeSignal 

            ft232h.output(8, GPIO.HIGH)

            time.sleep(0.1)

            ft232h.output(8, GPIO.LOW)

            #print 'camera fired'

            #time.sleep(1.95)

            if startIndex < 1000:
                photoFileName = 'DSCF0' + str(startIndex) + '.jpg'
            else:
                photoFileName = 'DSCF' + str(startIndex) + '.jpg'

            while not os.path.exists(photoFileName):
                pass
            

            fileCreationTime = datetime.datetime.fromtimestamp(os.stat(photoFileName).st_ctime)

            elapsedTime = fileCreationTime - timeSignal

            print 'file creation time: ', fileCreationTime , ' elapsed time: ' , elapsedTime

            # print 'file creation time: ', fileCreationTime

            print >> f, timeSignal ,' , ', fileCreationTime, ' , ' , elapsedTime

            #print >> f, timeSignal ,' , ', fileCreationTime

            startIndex = startIndex + 1

            #print 'cycle complete'

