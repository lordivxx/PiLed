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

# initialize GPIO pins as output pins
GPIO.setup(GREEN_LED, GPIO.OUT)

output = subprocess.check_output(['ps', '-A'])
if 'ntpd' in output:
    GPIO.output(GREEN_LED, True)
else:
    GPIO.output(GREEN_LED, False)


#exit
