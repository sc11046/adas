# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# 사용할 핀번호 대입

LED1 = 11
LED2 = 13
LED3 = 15
 
# 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
led =[LED1,LED2,LED3]
GPIO.setup(led ,GPIO.OUT, initial=GPIO.LOW)
# num=int(input('number'))
# for i in range(num):
while 1:
    GPIO.output(LED1, GPIO.HIGH)
    time.sleep(1)   
    GPIO.output(LED1, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED3, GPIO.LOW)
    time.sleep(1)   