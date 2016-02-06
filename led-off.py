#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
Blue_LED = 22
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(Blue_LED, GPIO.OUT)

GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)
GPIO.output(Blue_LED, False)
