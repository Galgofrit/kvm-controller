#!/usr/bin/env python

# Script used to change display settings from Windows->macOS (Samsung G7 displayPort->HDMI), and trigger a KVM switch.

import subprocess
import serial
import serial.tools.list_ports
import time
import sys

CONTROLMYMONITOR_UTIL = r"C:\Users\Gal\Coding\Utilities\controlmymonitor\ControlMyMonitor.exe"
VCP_VALUE_ID = 60
VCP_HDMI_ID = 6

def get_serial_port():
    com_ports = serial.tools.list_ports.comports()
    #import ipdb; ipdb.set_trace()
    for port in com_ports:
        if 'CH340' in port[1]:
            return port[0]
            
    return None

def trigger_kvm_switch():
    serial_port_path = get_serial_port()
    if not serial_port_path:
        print('Could not get serial port.')
        return 1

    print('Connecting to COM port', serial_port_path)
    arduino = serial.Serial(serial_port_path, 9600)
    arduino.write(1)
    time.sleep(5)   
    arduino.close()
    return 0

def switch_monitor():
    subprocess.call([CONTROLMYMONITOR_UTIL, '/SetValue', 'Primary', '60', '6'])


def main():
    switch_monitor()
    trigger_kvm_switch()

if __name__=='__main__':
    sys.exit(main())
