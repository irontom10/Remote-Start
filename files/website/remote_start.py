import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
RELAY_KEYSWITCH = 17  # Relay 1 control pin
RELAY_START = 27      # Relay 2 control pin
SENSE_PIN = 22        # Sense wire input pin

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_KEYSWITCH, GPIO.OUT)
GPIO.setup(RELAY_START, GPIO.OUT)
GPIO.setup(SENSE_PIN, GPIO.IN)

# Check Sense Wire Status
if GPIO.input(SENSE_PIN) == GPIO.LOW:
    # Sense wire is LOW, safe to proceed
    # Engage keyswitch relay
    GPIO.output(RELAY_KEYSWITCH, GPIO.HIGH)
    time.sleep(1)  # Wait for relay to stabilize

    # Send start pulse
    GPIO.output(RELAY_START, GPIO.HIGH)
    time.sleep(1)  # Duration of start pulse
    GPIO.output(RELAY_START, GPIO.LOW)

    # Keep keyswitch relay engaged for engine to run
    # Optionally, implement a timer or condition to disengage
else:
    print("Keyswitch is ON. Remote start disabled.")

GPIO.cleanup()
