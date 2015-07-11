# Rapberry Pi - Hello World. 
import RPi.GPIO as GPIO
import time

led_pin = 12

#function to toggle the pin
def blink(pin):
	GPIO.output(pin, GPIO.HIGH)
	# GPIO.output(pin, True) can also be used 
	time.sleep(1)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	return

#Turn off the warnings, better not to
#GPIO.setwarnings(False)

# GPIO.BCM option means that the pins are referred by 
# "Broadcom SOC channel number". GPIO4,GPIO18, ..etc.
# GPIO.setmode(GPIO.BCM)

# specifies pins are referred as the numbers of the male pin header
GPIO.setmode(GPIO.BOARD)

#set up the GPIO channel as output
GPIO.setup(led_pin,GPIO.OUT)

counter = 0
#infinite loop
try:
	while True:
		blink(led_pin)
		counter +=1
	
except KeyboardInterrupt:
	#code here will run before the program exits
	print "\nCounter value: %d" % counter	


except:
	#catches all other exceptions and errors
	print "Something went wrong!!!"

finally:
	GPIO.cleanup() # clean exit ensured
	print "All outputs are cleared as input-safe method"


#finite loop
#for i in range(0,10):
#	blink(led_pin)


