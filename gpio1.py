# GPIO 2 proqrami, daha yaxshi ishleyen

# kitabxana elavesi
import RPi.GPIO as GPIO     # GPIO qisaltmasindan istifade et
import time 		        # sleep(saniye) funksiyasi ucun

# pin nomresi
ledPin = 12
tekrar = 6

# Funksiya teyinati
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return


# pin teyinati
saygac = 0
GPIO.setwarnings(False)         # xeberdarliqlari sondur
GPIO.setmode(GPIO.BOARD)        # fiziki pin nomrelenme sxemi
GPIO.setup(ledPin, GPIO.OUT)    # pin 12 cixish olaraq teyin edilir

# sonsuz/sonlu dovre - try, except bloku ile
try:
    while True:
        blink(ledPin)
        saygac = saygac + 1
        print saygac


except KeyboardInterrupt:
    print "Proqram saxlanildi!" 

finally:
    GPIO.cleanup()              # pinlerin veziyyetini sifirla
    print "Pinler sifirlandi"

# Proqrami yarida saxlamaq ucun Ctrl+C
