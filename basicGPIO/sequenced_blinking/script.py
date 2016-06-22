import RPi.GPIO as GPIO
import time #for sleep
# Pin Definitons:
LEDPin = 17 # Broadcom pin 17
LED2Pin = 27
LED3Pin = 22
#this code isn't the best way to do this but it's the simplest way to demonstrate basic LED GPIO stuff clearly

# Pin Setup:
GPIO.setmode(GPIO.BCM) # use broadcom numbers instead of physical pins
GPIO.setup(LEDPin, GPIO.OUT)  #
GPIO.setup(LED2Pin, GPIO.OUT) # LED pins set as outputs
GPIO.setup(LED3Pin, GPIO.OUT) #

# Initial state for LEDs: we're doing it this way because weve set up the LEDs to be common positive so setting the pins the negative 'legs' are connected to "on" turns off the LEDS
GPIO.output(LEDPin, GPIO.HIGH)
GPIO.output(LED2Pin, GPIO.HIGH)
GPIO.output(LED3Pin, GPIO.HIGH)

print("Press CTRL+C to exit")
try:
    while True: #while loop which is always true
	    GPIO.output(LEDPin, GPIO.LOW) #switch the LED connected to pin 17 on
            time.sleep(1) #wait 1 second
	    GPIO.output(LED2Pin, GPIO.LOW) # switch the LED connected to pin 27 on 
	    time.sleep(1)
 	    GPIO.output(LED3Pin, GPIO.LOW) # Pin 22
	    time.sleep(1)
	    GPIO.output(LEDPin, GPIO.HIGH)	#
	    GPIO.output(LED2Pin, GPIO.HIGH)     # switch all three off again  	
	    GPIO.output(LED3Pin, GPIO.HIGH)     #
	    time.sleep(1)
          
           
except KeyboardInterrupt: # If CTRL+C is pressed, clean up so you don't get weird errors later
    GPIO.cleanup() # cleanup all GPIO

