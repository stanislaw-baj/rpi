import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.OUT)

def led_on():
    GPIO.output(21, GPIO.HIGH)
    print "LED on"

def led_off():
    GPIO.output(21, GPIO.LOW)
    print "LED off"

def cleanup():
    GPIO.cleanup()

def register_port_listener():
    def on_signal_received():
        print "Zmiana na port 20"
    GPIO.add_event_detect(20, GPIO.BOTH)
    GPIO.add_event_callback(20, on_signal_received)
