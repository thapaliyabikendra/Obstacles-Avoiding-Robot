import RPi.GPIO as gpio
import time

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

def right(tf):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()

def left(tf):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()

def forward(tf):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()

left(1.25)
#right(1.25)
#forward(1.25)
#reverse(3)
