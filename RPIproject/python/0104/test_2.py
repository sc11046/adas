import time
import RPi.GPIO as GPIO
# 핀번호 할당법은 커넥터 핀번호로 설정
# A B C D E F G DP
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# 핀 설정
seg = [10,9,11,15,14,18,23,24] # GPIO pin
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

# A B C D E F G DP
fnd = [(1,1,1,1,1,1,0,0), #0
    (0,1,1,0,0,0,0,0), #1
    (1,1,0,1,1,0,1,0), #2
    (1,1,1,1,0,0,1,0), #3 
    (0,1,1,0,0,1,1,0), #4
    (1,0,1,1,0,1,1,0), #5
    (1,0,1,1,1,1,1,0), #6
    (1,1,1,0,0,1,0,0), #7
    (1,1,1,1,1,1,1,0), #8
    (1,1,1,1,0,1,1,0)] #9

# 핀 출력
GPIO.output(seg,fnd[2])
# GPIO pin setting
