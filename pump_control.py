#!/usr/bin/python

import sys
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

HIGH = True # High Pegel
LOW = False # LOw Pegel

R_CH1 = 17
R_CH2 = 22
GPIO.setup(R_CH1, GPIO.OUT)
GPIO.setup(R_CH2, GPIO.OUT)

GPIO.output(R_CH1, int(sys.argv[1]))
# don't cleanup, so port stays in desired level after exit
#GPIO.cleanup()
