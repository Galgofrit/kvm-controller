#!/usr/bin/env python3

# Script used to change display settings from macOS->Windows (Samsung G7 HDMI->displayPort), and trigger a KVM switch.

import subprocess
import serial
import serial.tools.list_ports

DDCCTL_UTIL = '/usr/local/bin/ddcctl'
MONITOR_ID = 1 # Assume Samsung G7 is first external display connected
MONITOR_DISPLAYPORT_ID = 9

def get_serial_port():
    com_ports = serial.tools.list_ports.comports()
    for port in com_ports:
        print(port)
        if 'cu.usbserial' in str(port):
            return port[0]


def trigger_kvm_switch():
    serial_port_path = get_serial_port()
    if not serial_port_path:
        print('Could not get serial port.')
        return

    arduino = serial.Serial(serial_port_path, 9600)
    arduino.write(1)
    arduino.close()

def switch_monitor():
    subprocess.call([DDCCTL_UTIL, '-d', str(MONITOR_ID), '-i', str(MONITOR_DISPLAYPORT_ID)]) # Assume 


def main():
    switch_monitor()
    trigger_kvm_switch()

if __name__=='__main__':
    exit(main())
