#!/usr/bin/python

import time
import os
import RPi.GPIO as GPIO
from MCP3008 import MCP3008 as MCP3008

GPIO.setmode(GPIO.BCM)

HIGH = True # High Pegel
LOW = False # LOw Pegel

R_CH1 = 17
R_CH2 = 22
GPIO.setup(R_CH1, GPIO.OUT)
GPIO.setup(R_CH1, GPIO.OUT)

# Variablendefinition
SCLK        = 18 # Serial Clock
MOSI        = 24 # Master-Out Slave-IN
MISO        = 23 # Master-In Slave-Out
CS          = 25 # Chip-Select

mcp3008 = MCP3008(SCLK, MOSI, MISO, CS)

def main():
    while True:
        print "-" * 80
        temp1 = mcp3008.read_tmp36(0)
        print "TMP36-1 Pool Bottom: ", temp1
        if temp1 > 250:
            GPIO.output(R_CH1, GPIO.HIGH)
        else:
            GPIO.output(R_CH1, GPIO.LOW)
        print "TMP36-2  Earth : ", mcp3008.read_tmp36(1)
        print "TMP36-3  Air : ", mcp3008.read_tmp36(2)
        print "TMP36-4  : ", mcp3008.read_tmp36(3)
        print "TMP36-5  : ", mcp3008.read_tmp36(4)
        print "TMP36-6  : ", mcp3008.read_tmp36(5)
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
