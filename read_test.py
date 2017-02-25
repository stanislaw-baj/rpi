import serial
import time
from gpio import led_on, led_off, cleanup


def write(ser, msg):
	ser.write(msg)


def write_and_read(ser, parameter):
	write(ser, parameter)
	data=ser.readline()

	return data

ser = serial.Serial(
	port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

counter=0
parameter = b'KTI\r'

while True:

	if counter % 2 == 1:
		parameter = b'KT\r'
	else:
		parameter = b'KTI\r'

	response = write_and_read(ser, parameter)
	print response
	if response == 'OK':
		led_on()
	else:
		led_off()
	time.sleep(3)
	counter += 1

ser.close()
