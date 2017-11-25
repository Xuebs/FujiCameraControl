import time

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.FT232H as FT232H

import datetime
import os

FT232H.use_FT232H()

ft232h = FT232H.FT232H()

ft232h.setup(7, GPIO.IN)
ft232h.setup(8, GPIO.OUT)

startIndex = eval(raw_input("Enter current index + 1: "))
count = 1

with open('testresults_2sec.txt', 'w') as f:

    print 'Camera control ready'

    while True:
        timeSignal = datetime.datetime.now()

        print'signal time: ', timeSignal 

        ft232h.output(8, GPIO.HIGH)

        time.sleep(0.1)

        ft232h.output(8, GPIO.LOW)

        #print 'camera fired'

        if startIndex < 1000:
            photoFileName = 'DSCF0' + str(startIndex) + '.jpg'
        else:
            photoFileName = 'DSCF' + str(startIndex) + '.jpg'

        time.sleep(1.9)
        # while not os.path.exists(photoFileName):
        #     pass
        
        fileCreationTime = datetime.datetime.fromtimestamp(os.stat(photoFileName).st_ctime)
        elapsedTime = fileCreationTime - timeSignal
        print 'file creation time: ', fileCreationTime , ' elapsed time: ' , elapsedTime
        print >> f, timeSignal ,' , ', fileCreationTime, ' , ' , elapsedTime

        # if os.path.exists(photoFileName):
        #     fileCreationTime = datetime.datetime.fromtimestamp(os.stat(photoFileName).st_ctime)
        #     elapsedTime = fileCreationTime - timeSignal
        #     print 'file creation time: ', fileCreationTime , ' elapsed time: ' , elapsedTime
        #     print >> f, timeSignal ,' , ', fileCreationTime, ' , ' , elapsedTime
        # else:
        #     print >> f, timeSignal, ' , photo not retreived in time, count:', count
        #     print 'photo not retreived in time, count: ', count

        startIndex = startIndex + 1
        count = count + 1

        #print 'cycle complete'
