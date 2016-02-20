#!/usr/bin/env python

# Created by Chuck Forsyth
# Code adapted from various sources

# Import python libs
import RPi.GPIO as GPIO
import subprocess


# start GPIO pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# define GPIO pins to variables
GREEN_LED = 18
Blue_LED = 22

# initialize GPIO pins as output pins
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(Blue_LED, GPIO.OUT)

output = subprocess.check_output(['ps', '-A'])
if 'sub-write.py' in output:
    GPIO.output(GREEN_LED, True)
else:
    GPIO.output(GREEN_LED, False)

#if 'sub-write.py' in output:
#    GPIO.output(Blue_LED, True)
#else:
#    GPIO.output(Blue_LED, False)

#exit
