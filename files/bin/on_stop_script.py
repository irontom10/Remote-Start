#!/usr/bin/env python3

import RPi.GPIO as GPIO
import logging
import datetime

# Configure logging
logging.basicConfig(
    filename='/var/log/remote_start.log',
    level=logging.INFO,
    format='%(asctime)s: %(message)s'
)

def main():
    try:
        # Log the stop event
        logging.info('Remote Start Service has stopped.')

        # GPIO Pin Definitions
        RELAY_KEYSWITCH = 17  # GPIO17
        RELAY_START = 27      # GPIO27

        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # Disable warnings if pins were already in use

        # Set up GPIO pins
        GPIO.setup(RELAY_KEYSWITCH, GPIO.OUT)
        GPIO.setup(RELAY_START, GPIO.OUT)

        # Reset GPIO outputs to LOW
        GPIO.output(RELAY_KEYSWITCH, GPIO.LOW)
        GPIO.output(RELAY_START, GPIO.LOW)

        # Clean up GPIO settings
        GPIO.cleanup([RELAY_KEYSWITCH, RELAY_START])

    except Exception as e:
        logging.error('An error occurred in on_stop_script.py: %s', e)

if __name__ == '__main__':
    main()
