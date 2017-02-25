import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)

def led_on():
    GPIO.output(21, GPIO.HIGH)
    print "LED on"

def led_off():
    GPIO.output(21, GPIO.LOW)
    print "LED off"

def cleanup():
    GPIO.cleanup()
