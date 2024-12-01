#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import logging
import sys
import subprocess

# Configure logging
logging.basicConfig(
    filename='/var/log/remote_start.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def main():
    try:
        # GPIO Pin Definitions
        RELAY_KEYSWITCH = 17  # GPIO17
        RELAY_START = 27      # GPIO27
        SENSE_PIN = 22        # GPIO22
        SERVICE_NAME = 'remote_start.service'

        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_KEYSWITCH, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(RELAY_START, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(SENSE_PIN, GPIO.IN)

        logging.info('Remote Start Service Started')

        # Start the remote start sequence if the sense wire is LOW
        if GPIO.input(SENSE_PIN) == GPIO.LOW:
            logging.info('Sense wire LOW, initiating remote start sequence.')

            # Engage keyswitch relay
            GPIO.output(RELAY_KEYSWITCH, GPIO.HIGH)
            time.sleep(1)  # Wait for relay to stabilize

            # Send start pulse
            GPIO.output(RELAY_START, GPIO.HIGH)
            time.sleep(1)  # Duration of start pulse
            GPIO.output(RELAY_START, GPIO.LOW)

            logging.info('Engine started, keeping keyswitch relay engaged.')

            # Monitor the sense wire
            while True:
                if GPIO.input(SENSE_PIN) == GPIO.HIGH:
                    # Sense wire has power, terminate the script
                    logging.info('Sense wire HIGH detected. Terminating script.')
                    subprocess.call(['sudo', 'systemctl', 'stop', SERVICE_NAME])

                time.sleep(1)  # Check every second

        else:
            # Sense wire is HIGH at startup
            logging.info('Sense wire HIGH at startup. Remote start aborted.')
            sys.exit(0)

    except Exception as e:
        logging.error('An error occurred: %s', e)
        sys.exit(1)

    finally:
        # Clean up GPIO settings
        GPIO.output(RELAY_KEYSWITCH, GPIO.LOW)
        GPIO.output(RELAY_START, GPIO.LOW)
        GPIO.cleanup()
        logging.info('Remote Start Service Stopped')

if __name__ == '__main__':
    main()
