import serial
import time
from image_processing import ImageProcessing


serial_port = "/dev/cu.usbmodem74239701"

teensy = serial.Serial(serial_port, baudrate=115200, timeout=.1)


def write_read(x):
    teensy.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = teensy.readline()
    return data


while True:
    value = ImageProcessing().do_capture()
    print(value)
    if value is None:
        write_read("0")
    else:
        write_read(str(value))
