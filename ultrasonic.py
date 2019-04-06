import RPi.GPIO as GPIO
import time
from config import THRESHOLD, TRIGGER, ECHO
 

 
def getDistance():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIGGER, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)
	StartTime = time.time()
	StopTime = time.time()
	while GPIO.input(ECHO) == 0:
		StartTime = time.time()
	while GPIO.input(ECHO) == 1:
		StopTime = time.time()
	TimeElapsed = StopTime - StartTime
	distance = ((TimeElapsed * 34300) / 2) - THRESHOLD
	GPIO.cleanup()
	print ("Measured Distance = %.1f cm" % distance)
	return distance

if __name__ == '__main__':
    getDistance()
