# kitabxana elavesi
import RPi.GPIO as GPIO 	# GPIO qisaltmasindan istifade et
import time 				# sleep(saniye) funksiyasi ucun

ledPin = 12					# pin nomresi
tekrar = 6

# pin teyinati
GPIO.setwarnings(False)  	# xeberdarliqlari sondur
GPIO.setmode(GPIO.BOARD) 	# fiziki pin nomrelenme sxemi
GPIO.setup(ledPin, GPIO.OUT)# pin 12 cixish olaraq teyin edilir

# sonsuz/sonlu dovre
for deyishen in range(0,tekrar):
    GPIO.output(ledPin, GPIO.HIGH)  # pin 12 qosh
    time.sleep(1)					# 1 san gozle
    GPIO.output(ledPin, GPIO.LOW)  	# pin 12 sondur
    time.sleep(1)

GPIO.cleanup()   					# pinlerin veziyyetini sifirla
print "Ok"

# Proqrami yarida saxlamaq ucun Ctrl+C
