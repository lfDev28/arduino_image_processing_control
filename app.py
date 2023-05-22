import serial
import time

serial_port = "/dev/cu.usbmodem74239701"

teensy = serial.Serial(serial_port, baudrate=115200, timeout=.1)


def write_read(x):
    teensy.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = teensy.readline()
    return data


while True:
    num = input("Enter a number: ")  # Taking input from user
    value = write_read(num)
    print(value)
