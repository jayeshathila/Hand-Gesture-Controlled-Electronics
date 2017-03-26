import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
for i in range(0,2):
	print "LED on"
	GPIO.output(15,GPIO.HIGH)
	time.sleep(0.5)
	print "LED off"
	GPIO.output(15,GPIO.LOW)
	time.sleep(0.5)
