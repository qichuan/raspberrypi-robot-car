import RPi.GPIO as GPIO
import time

right_backward=7
right_forward=11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(right_forward, GPIO.OUT)
#GPIO.setup(right_backward, GPIO.OUT)
time.sleep(2)
GPIO.setup(right_forward, GPIO.IN);

GPIO.setup(right_backward, GPIO.OUT);
time.sleep(2)
GPIO.setup(right_backward, GPIO.IN);

#GPIO.output(right_forward, True)
#GPIO.output(right_backward, False)
#time.sleep(2)
#GPIO.output(right_forward, False)
#GPIO.output(right_backward, False)

