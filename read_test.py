import serial
import time

def write(ser, msg):
	ser.write(msg)

def write_and_read(ser):
	write(ser, b'KTI\r')
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

while True:
	print(write_and_read(ser))
	time.sleep(3)

ser.close()
