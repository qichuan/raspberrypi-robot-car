from fake_rpi import FGPIO
#import RPi.GPIO as GPIO
import time


GPIO = FGPIO()

right_backward_pin=7
right_forward_pin=11

left_backward_pin=16
left_forward_pin=18
	
class Motor:
	@staticmethod
	def initialization():
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
	
	def right_fwd_start(self):
		GPIO.setup(right_forward_pin, GPIO.OUT)
	
	def right_fwd_stop(self):
		GPIO.setup(right_forward_pin, GPIO.IN);
	
	def right_bck_start(self):
		GPIO.setup(right_backward_pin, GPIO.OUT);
	
	def right_bck_stop(self):
		GPIO.setup(right_backward_pin, GPIO.IN);

	def left_fwd_start(self):
		GPIO.setup(left_forward_pin, GPIO.OUT)
	
	def left_fwd_stop(self):
		GPIO.setup(left_forward_pin, GPIO.IN);
	
	def left_bck_start(self):
		GPIO.setup(left_backward_pin, GPIO.OUT);
	
	def left_bck_stop(self):
		GPIO.setup(left_backward_pin, GPIO.IN);


