import RPi.GPIO as GPIO
import time

class Motor:
	right_backward_pin=7
	right_forward_pin=11
	
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
	
	def right_fwd_start():
		GPIO.setup(right_forward_pin, GPIO.OUT)
	#GPIO.setup(right_backward, GPIO.OUT)
	#time.sleep(2)
	def right_fwd_stop():
		GPIO.setup(right_forward_pin, GPIO.IN);
	
	def right_bck_start():
		GPIO.setup(right_backward_pin, GPIO.OUT);
	#time.sleep(2)
	def right_back_stop():
		GPIO.setup(right_backward_pin, GPIO.IN);

#GPIO.output(right_forward, True)
#GPIO.output(right_backward, False)
#time.sleep(2)
#GPIO.output(right_forward, False)
#GPIO.output(right_backward, False)

