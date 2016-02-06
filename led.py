#!/usr/bin/env python

# Created by Chuck Forsyth
# Code adapted from various sources

# Import python libs
import time
import argparse
import RPi.GPIO as GPIO

# define argparse items
parser = argparse.ArgumentParser(description='This is a LED script by LORDIVXX.')
parser.add_argument('-t','--timer', help='How fast the lights blink',required=True)
parser.add_argument('-l','--lenght',help='How long the lights blink for', required=True)
args = parser.parse_args()

# define variables , taken from command line arguments, using argparse
TIMER = float(args.timer)
count = float(args.lenght)

# start GPIO pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# define GPIO pins to variables
GREEN_LED = 18
RED_LED = 23
Blue_LED = 22


# initialize GPIO pins as output pins
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(Blue_LED, GPIO.OUT)

# Run the blink loop for the defined amount of time
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

# turn off the Leds
GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)
GPIO.output(Blue_LED, False)


#exit
