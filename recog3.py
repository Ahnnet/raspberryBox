import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
import time


recognizer = cv2.face.LBPHFaceRecognizer_create()
# yml 파일 read
recognizer.read('trainer/trainer.yml')
# haarcascade read
path = '../opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(path)
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> loze: id=1,  etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
# names = ['None', 'loze', 'ljy', 'chs', 'ksw']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# servoMotor 함수
def servoMotor(pin, degree, t):
    GPIO.setmode(GPIO.BOARD) # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
    GPIO.setup(pin, GPIO.OUT) # GPIO 통신할 핀 설정
    pwm=GPIO.PWM(pin, 50) # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정

    pwm.start(3) # 초기 시작값, 반드시 입력해야됨

    pwm.ChangeDutyCycle(degree) # 보통 2~12 사이의 값을 입력하면됨
    time.sleep(t) # 서보모터가 이동할만큼의 충분한 시간을 입력. 너무 작은 값을 입력하면 이동하다가 멈춤

    # 아래 두줄로 깨끗하게 정리해줘야 다음번 실행할때 런타임 에러가 안남
    pwm.stop()
    GPIO.cleanup(pin)

flag=0
open=False
while True:
    recog = False
    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (open == False and confidence < 100):
            # id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            servoMotor(16, 8, 1) # open - 신호선을 16번 핀에 연결, 8의 각도로 1초동안 실행
            open = True
            time.sleep(10)
            recog = True
            

        else:
            id = "unknown"
            # cv2.putText("close")  
            servoMotor(16, 3.0, 1) # close

        
        # cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        # cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    

    # if(recog and flag>20):
    #     servoMotor(16, 8, 1) # open - 신호선을 16번 핀에 연결, 8의 각도로 1초동안 실행
    #     flag=0
    #     time.sleep(10)

    if(not recog and open):
        flag+=1

        if(flag>5):
            servoMotor(16, 3.0, 1) # close
            open = False
            cam.release()
            cam = cv2.VideoCapture(0)
            flag=0

    # if(not recog): servoMotor(16, 3.0, 1) # close
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

    # time.sleep(5)
# Do a bit of cleanup



print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()