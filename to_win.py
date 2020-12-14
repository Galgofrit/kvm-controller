#!/usr/bin/env python

import serial
import serial.tools.list_ports

def get_serial_port():
    com_ports = serial.tools.list_ports.comports()
    for port in com_ports:
        print(port)
        if 'cu.usbserial' in str(port):
            return port[0]


def main():
    serial_port_path = get_serial_port()
    if not serial_port_path:
        print('Could not get serial port.')
        return

    arduino = serial.Serial(serial_port_path, 9600)
    arduino.write(1)
    arduino.close()


if __name__=='__main__':
    exit(main())
