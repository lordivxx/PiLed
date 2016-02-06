#!/usr/bin/env python

# Created by Chuck Forsyth
# Code adapted from various sources 

import time
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser(description='This is a LED script by LORDIVXX.')
parser.add_argument('-t','--timer', help='How fast the lights blink',required=True)
parser.add_argument('-l','--lenght',help='How long the lights blink for', required=True)
args = parser.parse_args()

TIMER = float(args.timer)
count = float(args.lenght)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
Blue_LED = 22
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(Blue_LED, GPIO.OUT)

while count > 0:
	GPIO.output(GREEN_LED, False)
	GPIO.output(RED_LED, True)
	GPIO.output(Blue_LED, False)
	time.sleep(TIMER)
	GPIO.output(GREEN_LED, True)
	GPIO.output(RED_LED, False)
	GPIO.output(Blue_LED, True)	
	time.sleep(TIMER)
	GPIO.output(GREEN_LED, False)
	GPIO.output(RED_LED, True)
	GPIO.output(Blue_LED, False)	
	count = count - 1	

GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)
GPIO.output(Blue_LED, False)
