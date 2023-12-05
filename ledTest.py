import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
import time

motor = 24
green_led = 17
red_led = 18


# GPIO.setmode(GPIO.BCM)
# GPIO.setup(green_led, GPIO.OUT)
# GPIO.setup(red_led, GPIO.OUT)
# GPIO.setup(motor, GPIO.OUT) # GPIO 통신할 핀 설정

# LED 함수
def LedOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(green_led, GPIO.OUT)
    GPIO.setup(red_led, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup(pin)

# servoMotor 함수
def servoMotor(pin, degree, t):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor, GPIO.OUT) # GPIO 통신할 핀 설정
    # GPIO.setmode(GPIO.BOARD) # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
    pwm=GPIO.PWM(pin, 50) # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정

    pwm.start(3) # 초기 시작값, 반드시 입력해야됨

    pwm.ChangeDutyCycle(degree) # 보통 2~12 사이의 값을 입력하면됨
    time.sleep(t) # 서보모터가 이동할만큼의 충분한 시간을 입력. 너무 작은 값을 입력하면 이동하다가 멈춤

    # 아래 두줄로 깨끗하게 정리해줘야 다음번 실행할때 런타임 에러가 안남
    pwm.stop()
    GPIO.cleanup(pin)

flag = 0
while(True):
    flag+=1
    if(flag%20==0): 
        LedOn(green_led)
        servoMotor(23, 11.0, 1) # open motor
        time.sleep(2)
    else:
        LedOn(red_led)
        servoMotor(23, 3.0, 1) # close motor
        time.sleep(2)
    print(flag)