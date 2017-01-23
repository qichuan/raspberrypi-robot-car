#from fake_rpi import FGPIO
import RPi.GPIO as GPIO
import time


right_forward_pin=13
right_backward_pin=15

left_forward_pin=16
left_backward_pin=18

	
class Motor:
	@staticmethod
	def initialization():
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(right_forward_pin, GPIO.OUT, initial=0)
		GPIO.setup(right_backward_pin, GPIO.OUT, initial=0)
		GPIO.setup(left_forward_pin, GPIO.OUT, initial=0)
		GPIO.setup(left_backward_pin, GPIO.OUT, initial=0)
	
	def right_fwd_start(self):
		#GPIO.setup(right_forward_pin, GPIO.OUT)
		GPIO.output(right_forward_pin, 1)
	
	def right_fwd_stop(self):
		#GPIO.setup(right_forward_pin, GPIO.IN)
		GPIO.output(right_forward_pin, 0)
	
	def right_bck_start(self):
		#GPIO.setup(right_backward_pin, GPIO.OUT)
		GPIO.output(right_backward_pin, 1)
	
	def right_bck_stop(self):
		#GPIO.setup(right_backward_pin, GPIO.IN)
		GPIO.output(right_backward_pin, 0)

	def left_fwd_start(self):
		#GPIO.setup(left_forward_pin, GPIO.OUT)
		GPIO.output(left_forward_pin, 1)
	
	def left_fwd_stop(self):
		#GPIO.setup(left_forward_pin, GPIO.IN);
		GPIO.output(left_forward_pin, 0)
	
	def left_bck_start(self):
		#GPIO.setup(left_backward_pin, GPIO.OUT)
		GPIO.output(left_backward_pin, 1)
	
	def left_bck_stop(self):
		#GPIO.setup(left_backward_pin, GPIO.IN)
		GPIO.output(left_backward_pin, 0)


