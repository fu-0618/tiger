import RPi.GPIO as GPIO
import time

left_pwm=13
leftfeas_pwm=13
right_pwm=13
rightfeas_pwm=13

GPIO.setmode(GPIO.BCM)
GPIO.setup([left_pwm,leftfeas_pwm,right_pwm,rightfeas_pwm],GPIO.OUT)

left_pwm=GPIO.pwm(left_pwm,50)
leftfeas_pwm=GPIO.pwm(leftfeas_pwm,50)
right_pwm=GPIO.pwm(right_pwm,50)
rightfeas_pwm=GPIO.pwm(rightfeas_pwm,50)

def move(duty:int,dir:str)->None:
    if dir=="forward":
       GPIO.output(left_pwm,leftfeas_pwm,right_pwm,rightfeas_pwm.true)
       left_pwm,leftfeas_pwm,right_pwm,rightfeas_pwm.start(60)
    elif dir=="right":
        GPIO.output(left_pwm,leftfeas_pwm.true)
        left_pwm,leftfeas_pwm.start(60)
        GPIO.outup(right_pwm,rightfeas_pwm.true)
        right_pwm,rightfeas_pwm.start(30)
    elif dir=="left":
        GPIO.output(right_pwm,rightfeas_pwm.true)
        right_pwm,rightfeas_pwm.start(60)
        GPIO.output(left_pwm,leftfeas_pwm.true)
        left_pwm,leftfeas_pwm.start(30)
    else:
        GPIO.output(left_pwm,leftfeas_pwm,right_pwm,rightfeas_pwm.fales)
        
left_pwm,leftfeas_pwm,right_pwm,rightfeas_pwm.cleanup()
if __name__=="_main_":
    duty,dir=input("duty,dir=").split(",")
    move(duty,dir)