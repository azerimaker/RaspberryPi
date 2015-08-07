#Raspberry Pi GPIO Example
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error while importing GPIO library, run with sudo")
import time

#------------------------------------------------------
#Print GPIO version info
#print "GPIO Version: " + str(GPIO.RPI_INFO)
print "RPi board rev: " + str(GPIO.RPI_INFO['P1_REVISION'])
#print str(GPIO.VERSION)
#------------------------------------------------------
#------------------------------------------------------
# Pin definitions and setup functions
ledPin = 12
counter = 0
n_times = raw_input("Enter total number of blinks: ")
sleepTime = raw_input("Enter sleep time: ")

#------------------------------------------------------
#------------------------------------------------------
#Simple blink function, takes pin number as argument
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    #GPIO.output(pin,True)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

#------------------------------------------------------
#------------------------------------------------------
# Advanced blink with pin, number of blinks and sleep interval in sec
def blink_ntimes(pin, n_times, sleepTime):
    for i in range(0, n_times):
        print "Iteration " + str(i+1)
        GPIO.output(pin,True)
        time.sleep(sleepTime)
        GPIO.output(pin,False)
        time.sleep(sleepTime)
    print "Done!"

#------------------------------------------------------
# Turns of all GPIO warnings, better not to
GPIO.setwarnings(False)

#------------------------------------------------------
# Mode select for pin numbering
#GPIO.setmode(GPIO.BCM) # pin numbering of Broadcom SOC, GPIO4,GPIO18, ..etc.
GPIO.setmode(GPIO.BOARD) # Better, will work with all RPis, pin number

# to detect which mode set by other python module,
# returns: GPIO.BOARD, GPIO.BCM or GPIO.UNKNOWN
mode = GPIO.getmode()
print mode

#------------------------------------------------------
# setup every used channel as input or output
GPIO.setup(ledPin,GPIO.OUT)
# initial value can also be set for every channel]
#GPIO.setup(channel,GPIO.OUT,initial=GPIO.HIGH)

# setting up more than one channel, this also applies to setting up
# multiple output channel states as high or low
#chan_list = [11,12] # tuples can also be used as: chan_list = (11,12)
#GPIO.setup(chan_list, GPIO.OUT)




#------------------------------------------------------
#------------------------------------------------------
try:
   # blink_ntimes(ledPin,int(n_times),float(sleepTime))
    while True:
        blink(ledPin)
        counter +=1

except KeyboardInterrupt:
    # CTRL+C related interrupt, will run before program exits
    print "\nProgram interrupted at %d" % counter

except:
    # catches all other exceptions
    print "\mUnknown error happened"

finally:
    GPIO.cleanup() # ensures clean exit
    ptint "Safe exit"


# For loop can also be used, usage:
#for i in range(0,50):
#    blink(12)


#------------------------------------------------------
# Clean up -> returns channels to be input with no pull down/up
#GPIO.cleanup()
#GPIO.cleanup((channel1,channel2))
#GPIO.cleanup([channel1,channel2])
