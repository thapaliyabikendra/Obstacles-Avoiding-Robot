import RPi.GPIO as GPIO
import time
 
GPIO_TRIGGER = 14
GPIO_ECHO = 15
 
def getDistance():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
	GPIO.setup(GPIO_ECHO, GPIO.IN)
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2
	GPIO.cleanup()
	print ("Measured Distance = %.1f cm" % distance)
	return (distance - 8 )
