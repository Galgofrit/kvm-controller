#!/usr/bin/env python3

# Script used to change display settings from macOS->Windows (Samsung G7 HDMI->displayPort), and trigger a KVM switch.

import subprocess
import serial
import serial.tools.list_ports
import os

HOMEBREW_PREFIX = os.environ.get('HOMEBREW_PREFIX')
DDCCTL_UTIL = 'bin/ddcctl'
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
        return False

    arduino = serial.Serial(serial_port_path, 9600)
    arduino.write(1)
    arduino.close()

def switch_monitor():
    import ipdb; ipdb.set_trace()
    if not HOMEBREW_PREFIX:
        print('Homebrew prefix not found.')
        return False

    ddcctl_fullpath = os.path.join(HOMEBREW_PREFIX, DDCCTL_UTIL)
    subprocess.call([ddcctl_fullpath, '-d', str(MONITOR_ID), '-i', str(MONITOR_DISPLAYPORT_ID)]) # Assume 

def main():
    if not switch_monitor():
        print('Could not switch monitor.')
    if not trigger_kvm_switch():
        print('Could not trigger KVM switch.')

if __name__=='__main__':
    exit(main())
